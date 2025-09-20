from django.db import models

class Service_Company(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()