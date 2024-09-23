from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create a custom form for the user so that email fields are also displayed in the register page
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User # specifies the model the form interacts with
        fields = ['username', 'email', 'password1', 'password2'] # password1 and password2 indicate the password entry and password confirmation fields

        