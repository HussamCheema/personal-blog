from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post, Category
from .forms import PostForm, CategoryForm
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


@login_required(redirect_field_name='back', login_url='login')
def createCategory(request):

    form = CategoryForm()
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['description']
        Category.objects.create(
            name = name,
            description = desc
        )
        
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/create_category_form.html', context)


@login_required(login_url='login')
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('home')
    return render(request, 'base/delete_category.html', {'obj': category})


@login_required(redirect_field_name='back', login_url='login')
def createPost(request):

    form = PostForm()
    categories = Category.objects.all()
    if request.method == 'POST':
        import pdb; pdb.set_trace()
        title = request.POST['title']
        description = request.POST['description']
        body = request.POST['body']
        categories = request.POST.getlist('category')
        category_objs = [Category.objects.get(name=cat) for cat in categories]

        post = Post.objects.create(
            author = request.user,
            title = title,
            description = description,
            body = body,
        )
        post.category.add(*category_objs)
        
        return redirect('home')

    context = {'form': form, 'categories': categories}
    return render(request, 'base/create_post_form.html', context)

@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.author:
        return HttpResponse('Your have no permission to delete this post')

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'base/delete_post.html', {'obj': post})


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


def privacy(request):
    
    context = {

    }
    return render(request, 'base/privacy_policy.html', context)


def adminPanel(request):
    
    context = {

    }
    return render(request, 'base/admin_panel.html', context)