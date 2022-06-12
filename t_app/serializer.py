# type:ignore
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,School,Student,Task,Company,Course
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

'''
    User serializer class
'''
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        many=True
        model = User
        fields =  ['id','username','email','phone','role']

'''
    registration serializer class
'''
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username','email','phone','password','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], phone = self.data.get('phone'),role = self.data.get('role'))
        return user
'''
    profile serializer class
'''
class ProfileSerializer(serializers.ModelSerializer):
    profile_pic = CloudinaryField('image')
    class Meta:
        model = Profile
        fields = ('name','location','bio','profile_pic','ebooks')

class StudentSerializer(serializers.ModelSerializer):
    image= CloudinaryField('image')
    class Meta:
        many=True
        model = Student
        ordering = ['id']
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    image= CloudinaryField('image')
    class Meta:
        many=True
        model = School
        ordering = ['id']
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    image= CloudinaryField('image')
    class Meta:
        many=True
        model = Company
        ordering = ['id']
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        many=True
        model = Course
        ordering = ['id']
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    image= CloudinaryField('image')
    class Meta:
        many=True
        model = Task
        ordering = ['id']
        fields = '__all__'