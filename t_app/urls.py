# type:ignore
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet,UserViewSet,StudentViewSet,CompanyViewSet,TaskViewSet,CourseViewSet,SchoolViewSet
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI,CustomAuthToken
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register('profile',ProfileViewSet,basename='profiles')
router.register('students',StudentViewSet,basename='students')
router.register('companies',CompanyViewSet,basename='companies')
router.register('schools',SchoolViewSet,basename='schools')
router.register('courses',CourseViewSet,basename='courses')
router.register('tasks',TaskViewSet,basename='tasks')
router.register('user',UserViewSet,basename='user')

urlpatterns=[
    path('',include(router.urls)),
    path('<int:id>',include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api-token-auth/', obtain_jwt_token),
    path('token/',CustomAuthToken.as_view(),name='token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)