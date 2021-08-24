from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy

# Create custom user model

class MyUserManager (BaseUserManager):
    # custom user not to take username . email unique
    def _create_user(self, email, password, **extra_fields):
        
        # create and save user's email password
        if not email:
            raise ValueError("The email must be set!")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Create super user
    def _create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # create and save user's email password
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super User Must have is_staff!")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super User Must have is_superuser!")

        return self._create_user(email, password, **extra_fields)


