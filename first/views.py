
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def show(request):
    return HttpResponse('<marquee><h1>Welcome To Python Web Developement<h1></marquee>')