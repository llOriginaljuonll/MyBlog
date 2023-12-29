from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id: int
    birth_date = models.DateTimeField(null=True, blank=True)
    profile_img = models.FileField()

    def __str__(self):
        return self.username