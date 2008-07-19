from django.contrib import admin
from announcements.models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "creation_date", "members_only")
    list_filter = ("members_only",)

admin.site.register(Announcement, AnnouncementAdmin)
