from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_posts/<int:page>/', views.home, name='list_posts'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('create-post/', views.createPost, name='create-post'),
    path('post/<str:pk>/', views.postDetail, name='post-detail'),

]
