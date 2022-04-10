from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post, Category

def home(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'base/home.html', context)


def postDetail(request, pk):

    post = Post.objects.get(id=pk)

    context = {
        'post': post
    }

    return render(request, 'base/post_detail.html', context)


def about(request):
    
    context = {

    }
    return render(request, 'base/about.html', context)


def contact(request):
    
    context = {

    }
    return render(request, 'base/contact.html', context)
