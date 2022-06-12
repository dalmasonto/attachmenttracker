# type:ignore
from django.contrib.auth import get_user_model 
from django.contrib.auth import login
from .models import Company, Course, Profile, School, Student, Task
#api imports
from rest_framework.decorators import api_view
from .permissions import IsAdminOrReadOnly
from .serializer import ProfileSerializer, RegisterSerializer,UserSerializer,CompanySerializer,SchoolSerializer,CourseSerializer,TaskSerializer,StudentSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, generics,permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import filters
# auth import
from knox.models import AuthToken
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
User = get_user_model()
'''
     view set returning all CRUD method on profile model
'''
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

'''
     view set returning all CRUD and search method on company model
'''
class CompanyViewSet(viewsets.ModelViewSet):
    search_fields = ['company_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
'''
     view set returning all CRUD and search method on school model
'''
class SchoolViewSet(viewsets.ModelViewSet):
    search_fields = ['school_name']
    filter_backends = (filters.SearchFilter,)
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

'''
     view set returning all CRUD and search method on student model
'''
class StudentViewSet(viewsets.ModelViewSet):
    search_fields = ['first_name','second_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

'''
     view set returning all CRUD and search method on task model
'''
class TaskViewSet(viewsets.ModelViewSet):
    search_fields = ['first_name','second_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

'''
     view set returning all CRUD and search method on course model
'''
class CourseViewSet(viewsets.ModelViewSet):
    search_fields = ['first_name','second_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

'''
    view set returning all CRUD and search method on user model
'''
class UserViewSet(viewsets.ModelViewSet):
    search_fields = ['email','username']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''
    registration api view to post new users
'''
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
'''
    Login  api view that inherits from KnoxLoginView to log in users
'''
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
'''
    custom api view to post user, generate token, confim token and login users
'''
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "role": user.role,
                "email": user.email,
                "username": user.username,
            }
        )