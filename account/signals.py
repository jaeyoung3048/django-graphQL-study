from django.dispatch import receiver
from django.db.models.signals import post_save

from account.models.user import User
from account.models.user_profile import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)
