from django.contrib import admin
from .models import *


@admin.register(Universities)
class UNIVERSITIESAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_filter = ['is_active']

