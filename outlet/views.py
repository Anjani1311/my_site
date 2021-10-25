from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorator import *
from .models import *
from .forms import *


import math
# Create your views here.


def newspart(request):
    All_news = News.objects.filter()
    params = {"All_news": All_news}
    return render(request, 'outlet/home.html', params)


@OnlyAuth
def signin(request):
    LM = LoginForm(request.POST or None)
    if request.method == 'POST':
        if LM.is_valid():
            UserName = request.POST.get('username')
            PassWord = request.POST.get('password')
            user = authenticate(request, username=UserName, password=PassWord)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username or Password is incorrect')
        else:
            messages.error(request, LM.errors)
    else:
        LM = LoginForm()
    context = {'form': LM}
    return render(request, 'auth/login.html', context)


@OnlyAuth
def signup(request):
    if request.method == 'POST':
        SF = SignupForm(request.POST)
        if SF.is_valid():
            isStudent = SF.cleaned_data.get('is_student')
            isTeacher = SF.cleaned_data.get('is_teacher')
            if isStudent:
                SignUpUser = SF.save(commit=False)
                SignUpUser.is_student = True
                SignUpUser.status = True
                SignUpUser.save()
            elif isTeacher:
                SignUpUser = SF.save(commit=False)
                SignUpUser.is_teacher = True
                SignUpUser.status = True
                SignUpUser.save()
            else:
                messages.warning(request, 'Please Select Your user Type')
                return redirect('signin')
            user = SF.cleaned_data.get('username')
            messages.success(request, 'Account Created for ' + user)
            return redirect('signin')
        else:
            messages.error(request, SF.errors)
    else:
        SF = SignupForm()
    context = {'form': SF}
    return render(request, 'auth/signup.html', context)


@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def index(request):
    All_news = News.objects.all()
    New_list = []

    catnews = All_news.values('category')
    cats = {item['category'] for item in catnews}
    for cat in cats:
        news = All_news.filter(category=cat)
        n = len(news)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        New_list.append([news, range(1, nSlides), nSlides])

    params = {"New_list": New_list}
    return render(request, 'outlet/index.html', params)


@login_required(login_url='signin')
def news_add(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('index')
    else:
        form = NewsForm(None)
    context = {'form': form}
    return render(request, "outlet/addnew.html", context)


@login_required(login_url='signin')
def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_edit', pk=pk)
    else:
        form = NewsForm(instance=news)

    context = {'form': form}
    return render(request, "outlet/addnew.html", context)




def about(request):
    return render(request, "outlet/about.html")


def contact(request):
    context = {"success": False}
    if request.method == 'POST':
        # access value from contact which is in name part
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        ins = Contact(person_name=name, person_email=email, person_phone=mobile,
                      message=message)  # named argument creating object
        ins.save()
        context = {"success": True}

    return render(request, "outlet/contact.html", context)


def search(request):
    return HttpResponse('We are in the Search page.')


def productview(request):
    return HttpResponse('We are in the product view page.')


def checkout(request):
    return HttpResponse('We are in the Checkout  page.')
