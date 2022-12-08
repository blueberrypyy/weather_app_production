from django.urls import path
from . import views

urlpatterns = [
        path('signup/', views.SignupView, name='signup'),
        path('login/', views.LoginView, name='login')
        ]
