from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import register_login,employee

router = DefaultRouter()

router.register('register', register_login.UserRegister, basename='register')
router.register('login', register_login.UserLogin, basename='login')


urlpatterns = [
    path('', include(router.urls)),
    path('employee/', employee.EmployeeList.as_view()),
    path('employee/<int:pk>/', employee.EmployeeDetail.as_view()),
    
]