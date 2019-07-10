from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return  HttpResponse('hello')

def master(request):
    return  HttpResponse('master')