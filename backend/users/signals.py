from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

@receiver(post_save, sender=User)
def add_default_requester_role(sender, instance, created, **kwargs):
    if not created:
        return

    # Optional: don't auto-assign to superusers/staff
    if instance.is_superuser:
        return

    requester, _ = Group.objects.get_or_create(name="REQUESTER")
    instance.groups.add(requester)
