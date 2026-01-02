from .settings import exluded_urns
from .models import Announcement
from django.utils import timezone

def announcements_processor(request):
    context = {}
    disable = False

    try:
        disable = request.COOKIES['disable_announcements']
    except:
        pass

    if request.path not in exluded_urns and not disable:
        context = {'announcements': Announcement.objects.filter(end_date__gt=timezone.now())}

    return context