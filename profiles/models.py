from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(_("name"), blank=True, null=True, max_length=150)
    bio = models.TextField(_("bio"), blank=True)


    # You can add additional fields here, such as:
    # - website
    # - social media links
    # - personal interests
    # - company position for B2B users
    # - etc.

    def __str__(self):
        return f"{self.user.username}'s Profile"

# You might want to create the UserProfile automatically when a new user is created.
# To achieve this, you can use Django's signals:


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
