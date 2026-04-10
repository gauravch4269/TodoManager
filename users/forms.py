from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomRegistrationForm(UserCreationForm):  #inherit UserCreationForm to use its feature
    email=forms.EmailField()
    class Meta:
        model = User   # ✅ THIS LINE IS REQUIRED
        fields = ['username', 'email','password1','password2']