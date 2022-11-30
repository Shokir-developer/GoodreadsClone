from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_email_welcome(sender, instance, created, **kwargs):
    print("SIGNALL")
    # send_mail(
    #     "Welcome to Goodreads clone",
    #     f"Hi ,user. Welcome to our website!",
    #     "begbotovshake@gmail.com",
    #     [instance.email]
    # )