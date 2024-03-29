from random import choice

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.support.models import ChatSupport, NotificationSupport
from apps.accounts.models import Account


@receiver(post_save, sender=ChatSupport)
def notification(sender, instance, created, **kwargs):
    if created:
        supports = Account.objects.filter(is_support=True)
        admins = Account.objects.filter(is_superuser=True)

        if not supports:
            NotificationSupport.objects.create(
                support_account=choice(admins),
                chat_support=instance,
            )
        
        else:
            NotificationSupport.objects.create(
                support_account=choice(supports),
                chat_support=instance,
            )