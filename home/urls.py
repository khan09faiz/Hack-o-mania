from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='About'),
    path("login",views.login,name='login'),
    path("contact",views.contact,name='Contact'),
    path("register",views.register,name='register'),
    
]