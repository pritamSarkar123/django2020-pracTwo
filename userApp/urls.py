from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'userApp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('loggout/', views.user_logout, name='loggout'),
]
