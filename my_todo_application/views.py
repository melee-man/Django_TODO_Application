from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Task
from django.views.generic import (
    ListView,
    DetailView
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
    for task in context['tasks']:
        print (task)

    return render(request, 'my_todo_application/home.html', context)


class UserTaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task

    def test_func(self):
        task = self.get_object()

        if self.request.user == task.user:
            return True
        return False


