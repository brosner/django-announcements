
from django.http import HttpResponse
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404

from announcements.models import Announcement


def announcement_list(request):
    announcements_hidden = request.session.get("announcements_hidden", set())
    queryset = Announcement.objects.exclude(pk__in=announcements_hidden)
    if not request.user.is_authenticated():
        queryset = queryset.filter(members_only=False)
    queryset = queryset.order_by("-creation_date")
    return list_detail.object_list(request, **{
        "queryset": queryset,
        "allow_empty": True,
    })

def announcement_hide(request, object_id):
    """
    Mark this announcement hidden in the session for the user.
    """
    announcement = get_object_or_404(Announcement, pk=object_id)
    announcements_hidden = request.session.get("announcements_hidden", set())
    announcements_hidden.add(announcement.pk)
    request.session["announcements_hidden"] = announcements_hidden
    return HttpResponse("hiding %s" % object_id)
