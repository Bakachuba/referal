from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(ReferralCode)
class BookAdmin(ModelAdmin):
    pass


@admin.register(Referral)
class BookAdmin(ModelAdmin):
    pass


@admin.register(UserProfile)
class BookAdmin(ModelAdmin):
    pass
