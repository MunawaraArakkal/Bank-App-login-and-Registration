
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def home(request):
    return render(request,"home.html")

@csrf_protect
@login_required(login_url='login')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('bankapp:newpage')
        else:
            return HttpResponse("Username or Password is incorrect!!! or you are not registered yet")

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email,pass1)
            my_user.save()
            return redirect('bankapp:login')
    return render(request,'register.html')


def newpage(request):
    return render(request,'newpage.html')
def form(request):
    return render(request,'form.html')











