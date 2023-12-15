from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    verified_member = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), blank=False)
    pass
    def __str__(self):
        return self.username
