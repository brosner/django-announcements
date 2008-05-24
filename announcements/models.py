
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class AnnouncementManager(models.Manager):
    def current(self, exclude=[], site_wide=False, for_members=False):
        """
        Fetches and returns a queryset with the current announcements.
        """
        queryset = self.all()
        if site_wide:
            queryset = queryset.filter(site_wide=True)
        if exclude:
            queryset = queryset.exclude(pk__in=exclude)
        if not for_members:
            queryset = queryset.filter(members_only=False)
        queryset = queryset.order_by("-creation_date")
        return queryset


class Announcement(models.Model):

    title = models.CharField(_("title"), max_length=50)
    content = models.TextField(_("content"))
    creator = models.ForeignKey(User, verbose_name=_("creator"))
    creation_date = models.DateTimeField(_("creation_date"), default=datetime.now)
    site_wide = models.BooleanField(_("site wide"), default=False)
    members_only = models.BooleanField(_("members only"), default=False)
    
    objects = AnnouncementManager()
    
    def get_absolute_url(self):
        return ("announcement_detail", [str(self.pk)])
    get_absolute_url = models.permalink(get_absolute_url)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _("announcement")
        verbose_name_plural = _("announcements")
    
    class Admin:
        list_display = ("title", "creator", "creation_date", "members_only")
        list_filter = ("members_only",)

def current_announcements_for_request(request, **kwargs):
    defaults = {}
    if request.user.is_authenticated():
        defaults["for_members"] = True
    defaults["exclude"] = request.session.get("excluded_announcements", set())
    defaults.update(kwargs)
    return Announcement.objects.current(**defaults)
