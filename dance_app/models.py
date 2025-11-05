from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    ROLE_CHOICES = [
        ('dancer', 'Dancer'),
        ('school', 'Dance School'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.name} ({self.role})"
        
class Dancer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    dance_style = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DanceSchool(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    dances_taught = models.TextField(help_text="List of dances taught, separated by commas")
    classes_per_week = models.PositiveIntegerField()

    def __str__(self):
        return self.name
