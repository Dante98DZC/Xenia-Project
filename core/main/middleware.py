from core.main.models import NotificationUser
from config.settings import TIME_LIMIT

class UserNotificationsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if not request.user.is_anonymous:
            response.context_data[
                "user_notifications"
            ] = NotificationUser.objects.filter(user=request.user)
            response.context_data[
                "time_limit"
            ] = TIME_LIMIT
        return response
