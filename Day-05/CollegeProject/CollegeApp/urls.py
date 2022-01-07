from django.urls import path
from CollegeApp import views

urlpatterns = [
	path('',views.home,name="hm"),
]