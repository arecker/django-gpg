from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from . import gpg


def validate_public_key(value):
    try:
        with gpg.client(import_keys=[value]):
            pass
    except ValueError as e:
        raise ValidationError(_(e.message))


class PublicKeyField(models.TextField):

    description = 'ASCII-armored formatted Public GPG Key'

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = (
            kwargs.get('validators', []) + [validate_public_key]
        )
        super(PublicKeyField, self).__init__(*args, **kwargs)
