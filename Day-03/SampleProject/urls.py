"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from SampleApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi),
    path('welcome/<str:name>/',views.welcome),
    path('number/<int:rollno>/',views.number),
    path('myinfo/<str:name>/<int:rollno>/',views.myinfo),
    path('htmlmsg/',views.htmlmsg),
    path('data/<str:empn>/<int:age>/',views.employee),
    path('reg/',views.register),
    path('bt/',views.boot),
    path('st/',views.stf),
    path('ty/',views.bty),
]


