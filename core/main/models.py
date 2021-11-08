from core.express.models import Report
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class NotificationSource(models.IntegerChoices):
    REPORT_CREATED = 1
    REPORT_TIME_EXPIRED = 2
    REPORT_SOLVED = 3


class Notification(models.Model):
    notification_source = models.IntegerField(choices=NotificationSource.choices)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    notification_time = models.DateField(auto_created=True,blank=True,null=True)


class NotificationUser(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
