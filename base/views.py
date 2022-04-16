from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post, Category
from .forms import PostForm
from django.core.paginator import Paginator


def home(request, page=1):

    posts = Post.objects.all()
    paginator = Paginator(posts, 5) # 5 users per page
    
    try:
        posts = paginator.page(page)
    except:
        # if we exceed the page limit we return the last page 
        posts = paginator.page(1)

    context = {
        'posts': posts,
    }
    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def createPost(request):

    form = PostForm()
    categories = Category.objects.all()
    if request.method == 'POST':
        category = Category.objects.create(name=request.POST['category'])
        post_title = request.POST['title']
        post_description = request.POST['description']
        post_body = request.POST['body']

        Post.objects.create(
            author=request.user,
            title=post_title,
            description=post_description,
            category=category,
            body=post_body,
        )
        
        return redirect('home')

    context = {'form': form, 'categories': categories}
    return render(request, 'base/create_post_form.html', context)


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
