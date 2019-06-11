from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Task, Status
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

def index(request):
    return render(request, 'my_todo_application/index.html')


@login_required
def userdashboard(request):
    context = {
        'tasks' : Task.objects.all(),
        'user' : request.user
    }
    return render(request, 'my_todo_application/home.html', context)


class UserTaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task
    

    def test_func(self):
        task = self.get_object()

        if self.request.user == task.user:
            return True
        return False

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_name',  'due_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.task_status = Status.objects.get(id=2)
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_name', 'task_status', 'due_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('user_dashboard')
    
   


