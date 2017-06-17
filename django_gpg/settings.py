from django.conf import settings as django_settings

SETTINGS = getattr(django_settings, 'django_gpg', {})
PUBLIC_KEY_REQUIRED = SETTINGS.get('PUBLIC_KEY_REQUIRED', True)
