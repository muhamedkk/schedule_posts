from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login ,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .decorator import authorization

from .models import *


@csrf_exempt
@login_required(login_url='/authentication/login')
def index(request):
    posts=Post.objects.filter(is_published = True)
    c={'posts':posts}
    return render ( request,'index.html',c)

def date_validation(request,publishing_time):
    current_time = datetime.now()
    publishing_time = datetime.strptime(publishing_time, '%Y-%m-%dT%H:%M')
    if publishing_time <= current_time:
        return True

@login_required(login_url='/authentication/login')
@csrf_exempt
def profile(request):

    user = User.objects.get(id=request.user.id)
    user_posts = Post.objects.filter(author=user)
    if request.method=='POST':
        post_content = request.POST['post']
        publishing = request.POST['publishing']
        
        if date_validation(request,publishing):
            messages.warning(request, 'The date must be in the future')
            return redirect ('app:profile')
        
        new_post = Post.objects.create(author=user,
                                       content= post_content,
                                       scheduled_time = publishing
                                       )
        messages.success(request, 'published')
        return redirect ('app:profile')
    c={'user':user,'posts':user_posts}
    return render ( request,'profile.html',c)

@csrf_exempt
@authorization
def edit_post(request,pk): 
    post=get_object_or_404( Post,id=pk)
    if date_validation(request,request.POST['publishing']):
        messages.warning(request, 'The date must be in the future')
        return redirect ('app:profile')
    post.content =  request.POST['post']
    post.scheduled_time = request.POST['publishing']
    post.is_published = False
    post.save()
    messages.success(request, 'Edited Post')
    return redirect ('app:profile')

@authorization
def delete_post(request,pk):
    post=get_object_or_404( Post,id=pk)
    post.delete()
    messages.success(request, 'Deleted Post')
    return redirect ('app:profile')
    
def login_fun(request,username,password):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return True
    return False

    
@csrf_exempt
def _login(request):
    if request.method=='POST':
        if login_fun(request,request.POST['username'],password=request.POST['password']):
            messages.success(request, 'welcome')
            return redirect ('app:profile')
        messages.success(request, 'Username Or Password invalid')
        return redirect ('app:login')
    return render ( request,'authentication/login.html')

@csrf_exempt
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            new_user=User.objects.create_user(username=username,password=password)
            login_fun(request,username,password=password)
            messages.success(request, 'welcome')
            return redirect ('app:profile')
        except:
            messages.success(request, 'Username Is Existing')
            return redirect ('app:login')
    return render ( request,'authentication/signup.html')

@csrf_exempt
def _logout(request):
    logout(request)
    return redirect('app:login')