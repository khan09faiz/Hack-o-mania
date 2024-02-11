from django.shortcuts import render ,HttpResponse
from home.models import login
def base(request):
    return render(request,'base.html')
def about(request):
   return  render(request,'about.html')
def login(request):
    return  render(request,'login.html')
def contact(request):
    return  render(request,'contact.html')
def register(request):
    return  render(request,'register.html')

