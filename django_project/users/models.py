from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,User
from django.core.validators import RegexValidator
# Create your models here.

class AccountUser(AbstractUser):
    #username = models.CharField(max_length = 120)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$', message="Phone number must be entered in the format: '+381...'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],max_length=17, blank=True) # validators should be a list
    location = models.CharField(max_length=60)

    #USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username