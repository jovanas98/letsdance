from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/dancer/', views.register_dancer, name='register_dancer'),
    path('register/school/', views.register_school, name='register_school'),
    path('schools/', views.school_list, name='school_list'),
    path('login/', views.login_view, name='login'),
]

