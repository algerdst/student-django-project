from django.contrib.auth.models import AbstractUser,Group,Permission

from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', default='default.jpg', null=True, blank=True)









