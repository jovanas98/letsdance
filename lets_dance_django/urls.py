
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin
    path('', include('dance_app.urls')),  
]