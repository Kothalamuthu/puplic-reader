from django import forms
from .models import info
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')

class UserInfoForm(forms.ModelForm):
     class Meta():
         model = info
         fields = ('last_name',)