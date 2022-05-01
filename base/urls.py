from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_posts/<int:page>/', views.home, name='list_posts'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy-policy'),
    path('create-post/', views.createPost, name='create-post'),
    path('delete-post/<str:pk>/', views.deletePost, name="delete-post"),
    path('create-category/', views.createCategory, name='create-category'),
    path('delete-category/<str:pk>/', views.deleteCategory, name="delete-category"),
    path('post/<str:pk>/', views.postDetail, name='post-detail'),
    path('admin/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin-panel/', views.adminPanel, name='admin-panel'),
]
