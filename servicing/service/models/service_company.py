from django.db import models

class ServiceCompany(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()