# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from models import GpgProfile


class GpgProfileInline(admin.StackedInline):
    model = GpgProfile
    can_delete = False
    verbose_name_plural = 'GPG Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (GpgProfileInline, )


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)
