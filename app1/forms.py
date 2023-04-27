from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='RE-ENTER PASSWORD',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class UpdateuserprofileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login','is_active']


class UpdateadminprofileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields ='__all__'