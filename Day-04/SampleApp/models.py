from django.db import models

# Create your models here.
class Employee(models.Model):
	empname = models.CharField(max_length=50)
	empage = models.IntegerField()
	empsal = models.IntegerField()
