from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import BoadModel
from django.contrib.auth.decorators import login_required

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
            return redirect('list')
        else:
            return render(request, 'login.html', {'context':'このユーザーは登録されていません'})

    return render(request, 'login.html', {})


@login_required
def listfunc(request):
    
    object_list = BoadModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})


def logoutfunc(request):

    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    
    object = get_object_or_404(BoadModel, pk=pk)
    return render(request, 'detail.html',{'object':object})

def goodfunc(request, pk):
    
    object = get_object_or_404(BoadModel, pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')