from django.urls import path
from . import views  # import views.py from this app

urlpatterns = [
    path('', views.home, name='home'),          # homepage
    path('register/', views.register, name='register'),  # register page
]