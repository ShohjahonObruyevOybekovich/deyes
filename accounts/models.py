from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.first_name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.role.name
