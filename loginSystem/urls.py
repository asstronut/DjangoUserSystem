from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'loginSystem'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='loginSystem/login.html'), name='login'),
    path('login/', auth_views.LogoutView.as_view(template_name='loginSystem/logout.html'), name='logout')
]