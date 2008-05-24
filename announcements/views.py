
from django.http import HttpResponseRedirect
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404

from announcements.models import Announcement


def announcement_list(request):
    queryset = Announcement.objects.current(request)
    return list_detail.object_list(request, **{
        "queryset": queryset,
        "allow_empty": True,
    })

def announcement_hide(request, object_id):
    """
    Mark this announcement hidden in the session for the user.
    """
    announcement = get_object_or_404(Announcement, pk=object_id)
    # TODO: perform some basic security checks here to ensure next is not bad
    redirect_to = request.GET.get("next")
    announcements_hidden = request.session.get("announcements_hidden", set())
    announcements_hidden.add(announcement.pk)
    request.session["announcements_hidden"] = announcements_hidden
    return HttpResponseRedirect(redirect_to)
