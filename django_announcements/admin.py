from django.contrib import admin
from .models import Announcement

class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['content', 'category', 'start_date', 'end_date', 'is_active']

admin.site.register(Announcement, AnnouncementsAdmin)
