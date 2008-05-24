
from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    creator = models.ForeignKey(User)
    creation_date = models.DateTimeField()

    def get_absolute_url(self):
        return "/announcements/" + str(self.pk)
    
    def __unicode__(self):
        return self.title
    
    class Admin:
        list_display = ("title", "creator", "creation_date")
