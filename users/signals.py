from django.db.models.signals import post_save # triggers a signal when data is saved
from django.contrib.auth.models import User # it is the sender that triggers the signal when a new user is saved
from django.dispatch import receiver # receives the signal triggered by the sender on save
from .models import Profile # model instance that gets created once signal is received

@receiver(post_save, sender=User)
# instance is the user instance created
# created is the flag that indicates the creation of the user instance
def create_profile(sender, instance, created, **kwargs): # create_profile is the receiver function
    if created:
        Profile.objects.create(user=instance)


# save profile signal everytime a user gets created

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()