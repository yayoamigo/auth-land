from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class BaseUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email = email,
            name = name
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user



class UserAccount(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    objects = BaseUserManager()

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email