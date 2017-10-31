from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """ helps django work with custom user model """

    def create_user(self, email, name, password=None):
        """ Create a new user profile object """

        if not email:
            raise ValueError('User must have an email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ creates and saves new superuser with  given details. """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user
        
        
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a User Profile inside our system."""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ use to get user full name """
        return self.name

    def get_short_name(self):
        """ use to get user short name """
        return self.name

    def get_email_field_name(self):
        """ use to get email address """
        return self.email

    def __str__(self):
        """ use to get object string represtion """
        return self.email


class ProfileFeedItem(models.Model):
    """Profile Status update."""
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns model as a string"""
        return self.status_text

