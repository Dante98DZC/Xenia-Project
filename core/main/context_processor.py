from datetime import date

from config.settings import TIME_LIMIT
from core.main.models import NotificationUser


def genaral_context(request):
    context = {}
    if not request.user.is_anonymous:
        context["user_notifications"] = NotificationUser.objects.filter(
            user=request.user
        )
        context["time_limit"] = TIME_LIMIT
        context["date"] = date.today()
    return context
