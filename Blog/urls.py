"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myBlog import views as myblog_views
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myblog_views.index),
    path('add/', myblog_views.add, name='add'),
    path('new_add/<int:a>/<int:b>/', myblog_views.add2, name='add2'),
    path('home/', myblog_views.index2, name='home'),
    re_path(r'add/(\d+)/(\d+)/', myblog_views.redirect),
]
