from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    message = "Rango says hey there partner!<br>" + \
              "Click <a href='/rango/about'>here</a> to know more about me."
    return HttpResponse(message)

def about(request):
    message = "Rango says here is the about page.<br>" + \
              "Click <a href='/'> here</a> to get back to the index page."
    return HttpResponse(message)
