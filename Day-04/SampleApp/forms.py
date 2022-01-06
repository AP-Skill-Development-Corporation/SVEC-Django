# from django.forms import ModelForm
from .models import Employee
from django import forms
class Eform(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ["empage","empname"]
		widgets = {
		"empname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Employee Name"
			}),
		"empage":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Employee Age"
			}),
		"empsal":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Employee Salary"
			}),
		}
