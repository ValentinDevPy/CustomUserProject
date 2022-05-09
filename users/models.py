from importlib._common import _

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    telephone_number = models.CharField(
        'Telephone number', unique=True,
        max_length=20,
    )
    consent = models.CharField(
        'Consent', max_length=64, unique=True,
    )
    first_name = models.CharField(max_length=64,)
    last_name = models.CharField(max_length=64,)
    email = models.EmailField('email address', unique=True)
    delete_flag = models.BooleanField(default=False)
    REQUIRED_FIELDS = [
        'email', 'telephone_number',
        'last_name', 'first_name', 'consent'
    ]
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
