from django.shortcuts import render,redirect
from .forms import UsForm
from django.contrib import messages
# Create your views here.
# from django.contrib.decorators import login_required

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		k = UsForm(request.POST)
		if k.is_valid():
			k.save()
			messages.success(request,"Registered Successfully")
			return redirect('/lgn')
	k = UsForm()
	return render(request,'html/register.html',{'h':k})