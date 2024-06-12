import email
import django
from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages
from category.models import District,Subdictrict,Gender
from django.core.files.storage import FileSystemStorage
 
# Create your views here.
def home(request):    
    return render(request,'home.html')

def dataSearch(request):    
    return render(request,'datasearch.html') 
     
def form(request):
    return render(request,'form.html')

def loginform(request):
    return render(request,'login.html')    

def addUser(request):
    email = request.POST['email']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    if password == repassword:
        if User.objects.filter(username = username).exists():
            messages.info(request,'duplicate username')           
            return redirect('/form')
        elif User.objects.filter(email = email).exists():
            messages.info(request,'duplicate email')            
            return redirect('/form')
        else:        
                user = User.objects.create_user(
                email = email,
                first_name = firstname,
                last_name = lastname,
                username = username,
                password = password
                )
                user.save()
                return redirect('/')
    else:
        messages.info(request,'mismatch password')        
        return redirect('/form')
 
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username,password=password)
        
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,'not found data')        
        return redirect('/loginform')
    
def logout(request):
    auth.logout(request)
    return redirect('/')



    
                        