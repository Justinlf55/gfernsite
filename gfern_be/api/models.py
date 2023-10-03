from django.db import models

# Create your models here.
class Admin(models.Model): 
    user_name = models.CharField(max_length=12, default="", unique=True)
    first_name = models.CharField(max_length=12, default="", unique=True)
    last_name = models.CharField(max_length=24, default="", unique=True)
    user_name = models.CharField(max_length=12, default="", unique=True)


