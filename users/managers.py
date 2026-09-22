from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email обязателен"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email обязателен"))
        if not extra_fields.get("phone_number"):
            raise ValueError(_("Суперпользователь обязан указать номер телефона"))
        if not str(extra_fields["phone_number"]).startswith("996"):
            raise ValueError(_("Телефон суперпользователя должен начинаться с 996"))

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
