from django.urls import path
from account import views


urlpatterns = [
    path('api/registration/', views.registration, name="register"),
    path('api/login/', views.login, name='login'), 
]