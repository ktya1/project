
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_login = None
    last_name = None

    photo = models.ImageField(
        upload_to='profile_photos/',
        default='profile_photos/default.png',  # фото по умолчанию
        blank=True,
        null=True,
    )
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username




    
#далее - setting :AUTH_USER_MODEL = 'users.User'




