from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id: int
    birthday = models.DateField(null=True, blank=True)
    profile_img = models.FileField()

    def __str__(self):
        return self.username