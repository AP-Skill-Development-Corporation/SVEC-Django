from django.shortcuts import render,redirect
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
	m = Employee.objects.all()[:5]
	if request.method == "POST":
		k = Eform(request.POST)
		if k.is_valid():
			k.save()
	k = Eform()
	return render(request,'html/eregister.html',{'p':k,'g':m})

def eupda(request,t):
	y = Employee.objects.get(id=t)
	d = Employee.objects.all()[:5]
	if request.method == "POST":
		m = Eform(request.POST,instance=y)
		if m.is_valid():
			m.save()
	m = Eform(instance=y) 
	return render(request,'html/eregister.html',{'p':m,'g':d})

def ede(request,b):
	v = Employee.objects.get(id=b)
	if request.method == "POST":
		v.delete()
		return redirect('/rgf')
	return render(request,'html/edte.html',{'y':v})
