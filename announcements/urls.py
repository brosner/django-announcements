
from django.conf.urls.defaults import *
from django.views.generic import list_detail

from announcements.models import Announcement


announcement_list_info = {
    "queryset": Announcement.objects.order_by("-creation_date"),
    "allow_empty": True,
}

announcement_detail_info = {
    "queryset": Announcement.objects.all(),
}

urlpatterns = patterns("",
    url(r"^(?P<object_id>\d+)/$", list_detail.object_detail,
        announcement_detail_info, name="announcement_detail"),
    url(r"^$", list_detail.object_list, announcement_list_info),
)
