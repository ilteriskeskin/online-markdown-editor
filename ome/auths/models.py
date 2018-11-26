from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=False, verbose_name='User', on_delete=True)
