from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from user.forms import UserRegisterForm,UserloginForm
from django.contrib.auth.models import User
from .models import ImageGallery

# Create your views here.
def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                return render(request,"register.html",{"form":form,"error_msg":"Username already exists"})  
            elif User.objects.filter(email=form.cleaned_data["email"]).exists():
                return render(request,"register.html",
                            {"form":form,"error_msg":"Email already exists"}
                ) 
            elif form.cleaned_data["password"]!=form.cleaned_data["password2"]:
                return render(request,"register.html",
                              {"form":form,"error_msg":"Password does not match"}
                        )
            else:
                user=User(
                    username=form.cleaned_data["username"],
                    email=form.cleaned_data["email"],
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    password=form.cleaned_data["password"]                  
                )
                user.save()
                auth_login(request,user)
                return redirect("home")
    form=UserRegisterForm()
    
    return render(request,"register.html",{"form":form})
def login(request):
    auth=UserloginForm()
    if request.method=="POST":
        form=UserloginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect("home")
            else:
                return render(request,"login.html",{"error_msg":"Incorrect username or password","auth":auth})
            
    return render(request,"login.html",{"auth":auth})


def home(request):
    if request.user.is_authenticated:
        image=ImageGallery.objects.all()
        if request.method=="POST":
            img=request.POST["photo"]
            ImageGallery.objects.create(Images=img)
        return render(request,"home.html",{"images":image})
    else:
        return redirect("login")