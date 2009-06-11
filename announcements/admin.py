
from django.contrib import admin

from announcements.models import Announcement
from announcements.forms import AnnouncementAdminForm

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "creation_date", "members_only")
    list_filter = ("members_only",)
    form = AnnouncementAdminForm
    fieldsets = [
            (None, {'fields': ['title', 'content', 'creator', 'creation_date', \
                               'site_wide', 'members_only' ]}),
            ('Manage announcement', {'fields': ['send_now']}),
        ]

admin.site.register(Announcement, AnnouncementAdmin)
