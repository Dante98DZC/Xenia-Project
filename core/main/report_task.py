import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from core.express.models import Report
from core.main.models import Notification, NotificationSource, NotificationUser
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone

current_timezone = timezone.get_current_timezone()


def notify_reports():
    reports = Report.objects.filter(
        Q(
            notification__report__isnull=True,
            solved=False,
            top_date_time__gte=current_timezone.localize(datetime.datetime.now()),
        )
        | Q(
            ~Q(
                notification__notification_source=NotificationSource.REPORT_TIME_EXPIRED
            ),
            notification__report__isnull=False,
            solved=False,
            top_date_time__gte=current_timezone.localize(datetime.datetime.now()),
        )
    )
    notifications = [
        Notification(
            notification_source=NotificationSource.REPORT_TIME_EXPIRED,
            report=report,
        )
        for report in reports
    ]
    notifications = Notification.objects.bulk_create(notifications)
    user_notification = [
        NotificationUser(notification=_notification, user=_user)
        for _user in User.objects.all()
        for _notification in notifications
    ]
    NotificationUser.objects.bulk_create(user_notification)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(notify_reports, "interval", seconds=1)
    # scheduler.start()
