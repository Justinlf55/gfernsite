from django.db import models

# Create your models here.
class User(models.Model): 
    user_name = models.CharField(max_length=12, default="", unique=True, null=False)
    first_name = models.CharField(max_length=12, default="", unique=True, null=False)
    last_name = models.CharField(max_length=24, default="", unique=True, null=False)
    user_name = models.CharField(max_length=12, default="", unique=True, null=False)
    email_address = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    password = models.CharField(max_length=100, default="", null=False)
    date_of_birth = models.CharField(max_length=30, blank=True, null=True, default=None)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

