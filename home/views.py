
from random import random

from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.models import User
from .models import *




def home(request):
    context={'blogs':BlogModel.objects.all()}
    return render(request,'home.html',context)

def login_page(request):
    try:
        if request.method=="POST":
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect ("/")
    except Exception as e:
        print(e)
    return render (request,'login.html')

def blog_detail(request,slug):
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context={'blog_obj': blog_obj}
    except Exception as e:
        print(e)
    return render (request,'blog_detail.html',context)


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email= request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        image = request.POST.get('image')
        post = request.POST.get('post')
        location = request.POST.get('location')
        experiance = request.POST.get('experiance')
        check_user = User.objects.filter(email=email).first()
        check_profile = Profile.objects.filter(mobile=mobile).first()
        if check_user or check_profile:
            context={'message':'user already exists','class':'danger'}
            return render (request,'register.html',context)
        user = User(username=username,email=email,first_name=name)
        user.set_password(password)
        user.save()
        profile = Profile(user = user,mobile=mobile,image=image,location=location,post=post,experiance=experiance)
        profile.save()
        return redirect('/login')
    return render (request,'register.html')

def see_blog(request):
    try:
        blog_objs=BlogModel.objects.filter(user=request.user)
        context={'blog_objs':blog_objs}

    except Exception as e:
        print(e)
    return render (request,'see_blog.html',context)

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')
def add_blog(request):
    context ={'form':BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image =request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            user_obj= BlogModel.objects.create(
                user=user,title=title,
                content = content,image=image
            )
            return redirect("/add-blog")

    except Exception as e:
        print(e)

    return render(request,'add_blog.html',context)

def blog_delete(request,id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user==request.user:
            blog_obj.delete()
        
    except Exception as e:
        print(e)
    return redirect("/see-blog")

def blog_update(request,slug):
    try:
        blog_obj = BlogModel.objects.get(slug=slug)

        if blog_obj.user != request.user:
            return redirect("/")
        initial_dict= {'content':blog_obj.content}
        form = BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image =request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            user_obj= BlogModel.objects.create(
                user=user,title=title,
                content = content,image=image
            )
        context={'blog_obj': blog_obj,'form':form}

    except Exception as e:
        print(e)
    return render (request,"update_blog.html",context)

def logoutpage(request):
    logout(request)
    return redirect ("/")

def user_profile(request,id):
    user=request.user
    user = Profile.objects.filter(id=id).first()
    context={'profile':user}
    return render (request,'user.html',context)
