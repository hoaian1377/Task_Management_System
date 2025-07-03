from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def task(request):
    return render(request,'task.html')
def login(request):
    return render(request,'login.html')