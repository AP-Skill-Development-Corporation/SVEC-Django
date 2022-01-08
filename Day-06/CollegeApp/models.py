from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	y = {
		(1,'Faculty'),
		(2,'Student'),
		(3,'Guest')
	}
	age = models.IntegerField(default=18)
	mobile = models.CharField(max_length=50)
	img = models.ImageField(upload_to="Profilepics",default='profile.jpg')
	usrole = models.IntegerField(choices=y,default=3)
