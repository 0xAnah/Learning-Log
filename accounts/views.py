from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # display a blank registration form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            redirect('learning_log:index')

    # display blank or invalid form
    context = {'form':form}
    return render(request, 'registration/register.html', context)
