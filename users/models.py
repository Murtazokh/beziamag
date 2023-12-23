from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    phone_number = models.CharField(_("phone number"), max_length=15, blank=True, null=True)
    address = models.TextField(_("address"), blank=True, null=True)
    profile_picture = models.ImageField(_("profile picture"), upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    email_verified = models.BooleanField(_("email verified"), default=False)

    def __str__(self):
        return self.username

