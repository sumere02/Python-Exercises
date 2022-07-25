from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def register(request):
    """
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            return redirect("index")
        else:
            context = {
            "form":form
            }
            return render(request,"register.html",context)    
    else:
        form = forms.RegisterForm()
        context = {
        "form":form
        }
        return render(request,"register.html",context)
    """
    form = forms.RegisterForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.info(request,"Registered Successfully")
            return redirect("index")
    else:
        context = {
        "form":form
        }
        return render(request,"register.html",context)
        
def loginUser(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"ID Or Password Is Incorrect")
            return render(request,"login.html",context)
        messages.info(request,"Welcome")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.info(request,"Exited")
    return redirect("index")
