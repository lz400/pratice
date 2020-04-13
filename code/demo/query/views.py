from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def qs(request):

    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('helo')

def weather(request, city, year):
    print(city)
    print(year)

    return HttpResponse('weather')

def get_body(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)


    return HttpResponse('haha')
