from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post

def home(request):

    context = {

    }
    return render(request, 'base/home.html', context)


def about(request):
    
    context = {

    }
    return render(request, 'base/about.html', context)


def contact(request):
    
    context = {

    }
    return render(request, 'base/contact.html', context)
