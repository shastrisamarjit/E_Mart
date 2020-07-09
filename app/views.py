from django.shortcuts import render,redirect
from app.forms import Adminform

def loginpage(request):
    return render(request,"app/loginpage.html",{"data":Adminform})