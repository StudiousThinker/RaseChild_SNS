from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import BoadModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username, '', password)
            return render(request, 'mylist.html', {})
        except IntegrityError:
            return render(request, 'signup.html',
                          {'error': 'このユーザーは既に登録されています'}
                          )
    return render(request, 'signup.html', {'context': 'get method'})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mylist')
        else:
            return render(request, 'login.html',
                          {'context': 'ユーザー名もしくはパスワードが間違っています'}
                          )
    return render(request, 'login.html', {})


@login_required
def listfunc(request):
    object_list = BoadModel.objects.all()
    if request.path_info == '/list/':
        html = 'list.html'
    else:
        html = 'mylist.html'
    return render(request, html, {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = get_object_or_404(BoadModel, pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodfunc(request, pk):
    object = get_object_or_404(BoadModel, pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')


class ContributeCreate(CreateView):
    template_name = 'create.html'
    model = BoadModel
    fields = ('title', 'content', 'contributor', 'priority')
    success_url = reverse_lazy('list')


class ContributeDelete(DeleteView):
    template_name = 'delete.html'
    model = BoadModel
    success_url = reverse_lazy('mylist')


class ContributeUpdate(UpdateView):
    template_name = 'update.html'
    model = BoadModel
    fields = ('title', 'content', 'priority')
    success_url = reverse_lazy('mylist')


def followfunc(request, pk):
    object = get_object_or_404(BoadModel, pk=pk)
    dummy = BoadModel.objects.create(title=object.title,
                                     content=object.content,
                                     contributor=request.user.username,
                                     priority=object.priority,
                                     follow=1)
    dummy.save()
    return redirect('mylist')
