from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from gpg import client


def validate_public_key(value):
    with client() as gpg:
        result = gpg.import_keys(value)
        if 'IMPORT_OK' not in result.stderr:
            msg = result.stderr.split('\n')[0]
            raise ValidationError(_(msg))


class PublicKeyField(models.TextField):

    description = 'ASCII-armored formatted Public GPG Key'

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = (
            kwargs.get('validators', []) + [validate_public_key]
        )
        super(PublicKeyField, self).__init__(*args, **kwargs)
