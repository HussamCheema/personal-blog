from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Category, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
