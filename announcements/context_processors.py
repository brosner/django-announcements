
from announcements.models import Announcement

def site_wide_announcements(request):
    ctx = {"site_wide_announcements": Announcement.objects.current(request, site_wide=True)}
    return ctx
