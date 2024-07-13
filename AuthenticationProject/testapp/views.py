from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

def front_view(request):
    return render(request,'testapp/front_page.html')

def login_view(request):
     if request.method=='POST':
         username=request.POST['userid']
         password=request.POST['password']
         user=authenticate(request,username=username,password=password)
         if user is not None:
             login(request,user)
             return redirect('home')
     return render(request,'testapp/login.html')


def registation_view(request):
    if request.method=='POST':
        userid=request.POST['userid']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password !=cpassword:
            return HttpResponse('<h2>Password And Confirm password not Match</h2>')
        print(userid,email,password)
        user=User.objects.create_user(username=userid,email=email,password=password)
        user.save()
        return redirect('login')
    return render(request,'testapp/registation.html')


def logout_view(request):
    logout(request)
    return redirect('front')

def home_view(request):
    return render(request,'testapp/home.html')
