from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm, SigninForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from duty.models import duty
from duty.forms import DutyForm
# Create your views here.

def homepage(request):
    form = DutyForm(request.POST or None)
    context = {
        'form':form
    }
    if request.user.is_authenticated:
        duties = duty.objects.filter(author = request.user)
        context['duties'] = duties
    if form.is_valid():
        author = request.user
        title = form.cleaned_data.get('title')
        statu = form.cleaned_data.get('statu')
        newduty = duty(author = author, title = title, statu = statu)
        newduty.save()
        messages.success(request, title + " eklendi!")
        return redirect("homepage")
    return render(request, 'home.html',context = context)

def djangopage(request):
    return render(request, 'djan.html')

def registerpage(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form,
        'title':'KAYIT OL',
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = User(username = username)
        user.set_password(password)
        user.save()
        return redirect('homepage')
    return render(request,"register.html", context = context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.error(request,"Kullanıcı zaten giriş yapmış")
        return redirect("homepage")
    form = SigninForm(request.POST or None)
    context = {
        'form':form,
        'title':'GİRİŞ YAP'
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username , password = password)
        if user:
            login(request, user)
            return redirect('homepage')
    return render(request,"register.html", context = context)

@login_required
def logoutpage(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız")
    return redirect("homepage")