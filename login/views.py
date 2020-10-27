from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def checker(request):
    val1=request.POST["username"]
    #check if username is free
    #store result in temp
    if 10>20:
        return redirect('/login')
    else:
        return redirect('/signup')
def index(request):
    val1=request.POST["username"]
    val2=request.POST["password"]
    #check if entry is present in database
    #store value in temp
    #fetch all records from database and pass them to index.html
    if 10>20:
        return render(request,'index.html',{'name':'Sarthak'})
    else :
        return redirect('/login')
def logout(request):
    return redirect('')
