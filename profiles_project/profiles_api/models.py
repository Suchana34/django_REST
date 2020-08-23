from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class Userprofilemanager(BaseUserManager):
    #helps django to work with our custom uder model

    def create_user(self, name, email, password = None):
        #creates a new user profile object
        if not email:
            raise ValueError('Users must give a email address')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, name, email, password):
        #creates and saves a new superuser with a given password and name

        user = self.create_user(name, email, password)

        user.is_superuser = True
        user. is_staff = True

        user.save(using = self._db)

        return user





class Userprofile(AbstractBaseUser, PermissionsMixin):
    #represents a user profile inside our system
    email = models.EmailField(max_length=254, unique= True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default= False)

    objects = Userprofilemanager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email