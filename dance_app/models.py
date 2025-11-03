from django.db import models

class Dancer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dance_style = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DanceSchool(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    contact_email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
