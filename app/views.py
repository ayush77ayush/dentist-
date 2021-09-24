from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from app.models import Patient
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html' )

def register(request):
    if request.method == 'POST':
        print('This is working')
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        print(first_name, last_name, email , password1 , mobile)

        if password1 == password2:
             user = User.objects.create_user(username = username, email = email, password = password1)
             user.first_name = first_name
             user.last_name = last_name
             user.mobile = mobile
             user.save()             
             extra =  Patient( first_name = first_name, last_name = last_name , email = email, mobile = mobile, password = password1)
             extra.save()   
             print('appointment done')
             return redirect('/')
        else:
            print('password does not match')
            return redirect('/register')

               
    else:
      print('something else is going on')
      return render(request, 'link.html' )

def loginfunc(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate( username = username, password = password)
        
        if user is not None:
             print('login in process')
             auth.login(request, user)
             return redirect('/')
             
        
        else:
            print('invalid')
            messages.info(request , 'invalid credentials')
            return redirect('login')


    else:    
       return render(request, 'login.html')
           
           



