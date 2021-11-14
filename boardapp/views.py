from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db import IntegrityError

# Create your views here.

def signupfunc(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username,'',password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています'})

    return render(request, 'signup.html', {'context':'get method'})

def loginfunc(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request,user)
            return render(request, 'login.html', {'context':'Loged in'})
        else:
            return render(request, 'login.html', {'context':'このユーザーは登録されていません'})

    return render(request, 'login.html', {'context':'get method'})

def listfunc(request):

    return render(request, 'list.html', {})
