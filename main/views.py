from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.forms import LoginForm, RegisterForm,FilesForm, ImageForm
from .models import UsersFiles, UsersImage
from django.conf import settings
import os


def registerPage(request):
    # инициализируем объект формы
    form = RegisterForm()
    if request.method == 'POST':
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)
        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    # ренедерим шаблон и передаем объект формы
    return render(request, 'main/registration.html', {'form': form})

def me(request):
    # если не авторизован, то редирект на страницу входа
    if not request.user.is_authenticated:
        return redirect('login')
    files=UsersFiles.objects.all()
    # рендерим шаблон и передаем туда объект пользователя
    return render(request, 'main/myFiles.html', {'user': request.user, 'files':files})

# выход
def myImagePage(request):
# если не авторизован, то редирект на страницу входа
    if not request.user.is_authenticated:
        return redirect('login')
    images=UsersImage.objects.all()
    # рендерим шаблон и передаем туда объект пользователя
    return render(request, 'main/myImage.html', {'user': request.user, 'images':images})

def doLogout(request):
    # вызываем функцию django.contrib.auth.logout и делаpем редирект на страницу входа
    logout(request)
    return redirect('login')

def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('me')
            else:
                form.add_error(None, 'Неверные данные!')
    return render(request, 'main/login.html', {'form': form})

def addFilesPage(request):
    if request.method=='POST':
        form=FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('me')
    else:
        form=FilesForm()
    return render(request, 'main/addFiles.html',{'form':form})

def deleteFilesPage(request, id):
    if request.method == 'POST':
        file=UsersFiles.objects.get(id=id)
        file.delete()
    return redirect('me')

def addImagePage(request):
    if request.method=='POST':
        form=ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myImage')
    else:
        form=ImageForm()
    return render(request, 'main/addImage.html',{'form':form})

def deleteImagePage(request, id):
    if request.method == 'POST':
        image=UsersImage.objects.get(id=id)
        image.delete()
    return redirect('myImage')


