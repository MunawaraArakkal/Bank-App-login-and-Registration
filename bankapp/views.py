from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
def newpage(request):
    return render(request,'newpage.html')
def form(request):
    return render(request,'form.html')
