
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class AnnouncementManager(models.Manager):
    def current(self, request=None, site_wide=False):
        """
        Fetches and returns a queryset with the current announcements.
        """
        queryset = self.all()
        if site_wide:
            queryset = queryset.filter(site_wide=True)
        if request:
            exclude = request.session.get("announcements_hidden", set())
            queryset = queryset.exclude(pk__in=exclude)
            if not request.user.is_authenticated():
                queryset = queryset.filter(members_only=False)
        queryset = queryset.order_by("-creation_date")
        return queryset


class Announcement(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    creator = models.ForeignKey(User)
    creation_date = models.DateTimeField(default=datetime.now)
    site_wide = models.BooleanField()
    members_only = models.BooleanField()
    
    objects = AnnouncementManager()
    
    def get_absolute_url(self):
        return ("announcement_detail", [str(self.pk)])
    get_absolute_url = models.permalink(get_absolute_url)
    
    def __unicode__(self):
        return self.title
    
    class Admin:
        list_display = ("title", "creator", "creation_date", "members_only")
        list_filter = ("members_only",)
