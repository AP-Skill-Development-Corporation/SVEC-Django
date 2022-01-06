from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import Eform


# Create your views here.
def hi(request):
	return HttpResponse("<h1 style='text-align:center;color:blue;'>hi abdul welcome to django</h1>")


def welcome(req,name):
	return HttpResponse("hi {} welcome to my lab".format(name))

def number(req,rollno):
	return HttpResponse(" hi this is my roll number {}".format(rollno))

def myinfo(req,name,rollno):
	return HttpResponse("Hi my name is {} and my roll number is {} ".format(name,rollno ))

def htmlmsg(req):
	return render(req,'html/htmlmsg.html')


def employee(request,empn,age):
	return render(request,'html/empdetails.html',{'en':empn,'a':age})

def register(request):
	if request.method == "POST":
		en = request.POST['empname']
		ea = request.POST['empage']
		es = request.POST['empsal']
		# print(en,ea,es)
		m = Employee(empname=en,empage=ea,empsal=es)
		m.save()
		rt = {'ena':en,'eag':ea,'esal':es}
		return render(request,'html/edetails.html',rt)
	return render(request,'html/register.html')

def boot(request):
	return render(request,'html/btexample.html')

def stf(request):
	return render(request,'html/stfm.html')

def bty(request):
	return render(request,'html/bt.html')

def eregister(request):
	k = Eform()
	return render(request,'html/eregister.html',{'p':k})


