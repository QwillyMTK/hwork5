from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class User(AbstractUser):
    is_active = models.BooleanField(default=False)  # при регистрации неактивен
    confirm_code = models.CharField(max_length=6, blank=True, null=True, unique=True)

    def generate_confirm_code(self):
        code = str(random.randint(100000, 999999))
        self.confirm_code = code
        return code
