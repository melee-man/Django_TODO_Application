from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #this saves the form data to the database
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created you are now able to log in!')
            return redirect('login') #redirects the user to the login page.
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})




