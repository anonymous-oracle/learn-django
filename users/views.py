from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # validates the data of the form across the various fields
            form.save() # saves the user; that's it
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account is created. You can now login")
            return redirect('login')


    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})