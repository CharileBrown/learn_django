# coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render #render是渲染模板
from django.urls import reverse

def index(request):
    return HttpResponse(u"这是欢迎界面！")

def index2(request):
    return render(request, 'home.html')#使用render会查找各个app下的templates

def add2(requeset, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def redirect(request, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))