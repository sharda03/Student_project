from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomeModel(AbstractUser):
    profile_pic=models.ImageField(upload_to='media/profile_pic')
    User= ((1,'HOD'),(2,'Staff'),(3,'Student'))
    user_type= models.CharField(choices=User,max_length=50,default=1)