import os
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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

@login_required # added so that the login page is shown to the user if at all the /profile route is accessed without authentication
def profile(request):
    if request.method.lower() == 'post':
        u_form = UserUpdateForm(request.POST, instance=request.user) # pass the current user instance to the form
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # request.POST sends the new data to be updated in user and user profile
        old_image_path=request.user.profile.image.path
        if os.path.exists(old_image_path):
            os.remove(old_image_path) # removes the image
        if u_form.is_valid() and p_form.is_valid():
            
            u_form.save()
            p_form.save()
            messages.success(request, "Your account details have been updated!")
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user) # returns a form prepopulated with the user's info
        p_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context=context)