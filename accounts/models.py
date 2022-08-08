
from __future__ import print_function
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from topics.models import Topic
from djoser.signals import user_activated
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import os

from dotenv import load_dotenv

load_dotenv()

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = os.getenv('API_KEY')

print(os.getenv('API_KEY'))

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "from the Python SDK!"
email_sender = {"name":"Zenitsu","email":"dakshchhabra158@gmail.com"}
replyTo = {"name":"Zenitsu","email":"dakshchhabra158@gmail.com"}
html_content = "<html><body><h1>Email Sent succesfully!! </h1></body></html>"




class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    email_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser,related_name='profile',on_delete=models.CASCADE)
    full_name = models.CharField(max_length=256,blank=True,null=True)

    solved_topics = models.ManyToManyField(Topic, related_name='users', blank=True)

    def __str__(self):
        return self.user.email








@receiver(user_activated)
def my_handler(user, request, **kwargs):
    UserProfile.objects.create(user=user)

# @receiver(user_activated, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
