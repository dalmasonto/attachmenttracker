# type:ignore
from pickle import TRUE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date, datetime as dt
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_school = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Course(models.Model):
    course_name = models.CharField(max_length=100)

class Company(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='company')
   company_name = models.CharField(max_length=30,blank=False,default='name')
   location = models.CharField(max_length=60,blank=True)
   phone = models.IntegerField(blank=False,default=0)
   image= CloudinaryField('image')


    
   def __str__(self):
       return f'{self.user.username} company'

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='school')
    school_name = models.CharField(max_length=30,blank=False,default='name')
    companies = models.ManyToManyField(Company,related_name='companies')
    courses = models.ManyToManyField(Company,related_name='courses')
    bio = models.TextField(max_length=255, default="Add Bio....", blank=True)
    image= CloudinaryField('image')
    phone = models.IntegerField(blank=False,default=0)


    
    
    def __str__(self):
        return f'{self.user.username} school'

class Student(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='student')
   first_name = models.CharField(max_length=30,blank=False,default='first name')
   second_name = models.CharField(max_length=30,blank=False,default='second name')
   school = models.ForeignKey(School,on_delete=models.CASCADE,default=1)
   image= CloudinaryField('image')
   phone = models.IntegerField(blank=False,default=0)

    
   def __str__(self):
       return f'{self.user.username} student'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=255, default="Add Bio....", blank=True)
    name = models.CharField(max_length=60,blank=True)
    location = models.CharField(max_length=60,blank=True)
    profile_pic= CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} profile'

class Task(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=60,blank=True)
    duration = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_complete= models.BooleanField(default=False)
    price = models.IntegerField()
    image = CloudinaryField('image')


    def __str__(self):
        return f'{self.title}'