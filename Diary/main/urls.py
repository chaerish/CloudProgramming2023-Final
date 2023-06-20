
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from main import views
app_name = 'main'

urlpatterns = [
    path('',views.main,name='main'),
    path('login/',auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/login.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
]
