# coding:utf-8
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"这是欢迎界面！")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(requeset, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))