import datetime

from django import template

register = template.Library()

@register.filter()
def duration(value:datetime.timedelta):
    if value is None:
        return 0
    return str(int(value.total_seconds()/60))
