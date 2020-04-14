from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):


    return HttpResponse('hello wold')

def get_values(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('hi')

def weather(request, year, city):
    print(city)
    print(year)
    return HttpResponse('xixi')

def get_data(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('response')
