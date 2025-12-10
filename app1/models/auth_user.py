from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class CustomerUserManager(BaseUserManager):
    def create_user(self, username,password,**extra_fields):
        if not username:
            raise ValueError("Username kiritilishi shart")
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is_superuser=True bolishi kerak')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff=True bolishi kerak')

        return self.create_user(username,password,**extra_fields)


class User(AbstractUser,PermissionsMixin):
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = CustomerUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.phone_number