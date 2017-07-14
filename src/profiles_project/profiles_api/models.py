from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# 1 customized user profile model
# to override the django built in user model
# 2 permission model

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""
        if not email: 
            raise ValueError('Users must have an email address.')
        
        # normalize email address to lower case to standardize
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # set_password convert a string to a hash
        # if anyone compromised the database they can't 
        
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)

        return user 


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a 'user profile' inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # An object manager is another class
    # to help manage the user profiles
    objects = UserProfileManager()

    # more attribute we need to set in our user profile
    # model class
    # USERNAME_FIELD is a handle or it's what the user 
    # uses to log in as.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # email is already set to required.

    # helper function

    # get the full name 
    def get_full_name(self):
        """Used to get a users full name"""
        return self.name 

    def get_short_name(self):
        """Used to get a users short name"""
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.email

    





