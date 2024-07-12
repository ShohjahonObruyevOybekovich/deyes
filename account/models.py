import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from account.managers import UserManager
class CustomUser(AbstractUser):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='media/profile_pics/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

    REQUIRED_FIELDS = []  # No additional required fields
    USERNAME_FIELD = 'username'  # Username is the unique identifier

    objects = UserManager()

    def __str__(self):
        return self.username