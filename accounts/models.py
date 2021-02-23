from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(Permissionsmixin, AbstractBaseUser):
    username = models.CharField()
    fullname = models.CharField()
    is_stuff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    phone_number_verified = models.BooleanField(default=False)
    phone_number = models.IntegerField