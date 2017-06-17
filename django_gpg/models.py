# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from settings import PUBLIC_KEY_REQUIRED
from fields import PublicKeyField
from . import gpg


User = get_user_model()


class GpgProfileQueryset(models.QuerySet):
    def encrypt(self, message, ignore_empty=False):
        keys = filter(None, self.values_list('public_key', flat=True))

        if not ignore_empty and self.count() != len(keys):
            raise ValueError('Not every User has a key')

        return gpg.encrypt(message, recipient_keys=keys)


class GpgProfile(models.Model):

    objects = GpgProfileQueryset.as_manager()

    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE
    )

    public_key = PublicKeyField(
        blank=(not PUBLIC_KEY_REQUIRED),
        null=(not PUBLIC_KEY_REQUIRED)
    )

    def __unicode__(self):
        return self.user.username

    def encrypt(self, message=''):
        return gpg.encrypt(message, recipient_keys=[self.public_key])

    class Meta:
        verbose_name = 'GPG Profile'


@receiver(models.signals.post_save, sender=User)
def save_gpg_profile(instance=None, created=False, **kwargs):
    if created:
        GpgProfile.objects.create(user=instance)
    else:
        instance.gpgprofile.save()
