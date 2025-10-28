from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('dancer', 'Dancer'),
        ('school', 'Dance School'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.role})"
