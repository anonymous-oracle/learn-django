from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# create a custom form for the user so that email fields are also displayed in the register page
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User # specifies the model the form interacts with
        fields = ['username', 'email', 'password1', 'password2'] # password1 and password2 indicate the password entry and password confirmation fields

        

# form for updating user info
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email'] # only update username and email
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image'] # allows to update the image field