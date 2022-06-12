# type:ignore
from django.contrib import admin

# Register your models here.
from .models import Profile,School,Company,Student,Task,Course,User


admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Course)
admin.site.register(User)
