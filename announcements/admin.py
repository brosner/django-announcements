
from django.contrib import admin

from announcements.models import Announcement
from announcements.forms import AnnouncmentAdminForm

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "creation_date", "members_only")
    list_filter = ("members_only",)
    form = AnnouncmentAdminForm

admin.site.register(Announcement, AnnouncementAdmin)
