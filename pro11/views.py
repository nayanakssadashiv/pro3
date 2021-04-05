from django.http import HttpResponse
from django.shortcuts import render
def index1(request):
    return  HttpResponse("hii good morning")
def rend_app1(request):
    return render(request,"home.html")