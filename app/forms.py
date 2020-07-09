from django import forms
from app.models import Adminlogin
from django.forms import PasswordInput

class Adminform(forms.ModelForm):
    class Meta:
        model=Adminlogin
        fields="__all__"
        labels={"name":"UserName","pas":"Password"}
        widgets={"pas":PasswordInput}