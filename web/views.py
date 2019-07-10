from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello')

def dev(request):
    return HttpResponse('dev')

