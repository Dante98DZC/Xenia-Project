import datetime

import pytz
from core.express.models import Report
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Count, Min, Sum
from django.db.models.query_utils import Q
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.timezone import make_aware
from django.views.generic import TemplateView


# Create your views here.
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_timezone = timezone.get_current_timezone()
        # """
        # {
        #     "today_not_solved_report":"",
        #     "today_solved_report":"",
        #     "reports_remaining":"",
        #     "today_new_report":"",
        # }
        # """
        today_not_solved_report = Count(
            "pk", Q(responsed=False,
                    top_date_time__lte=current_timezone.localize(datetime.datetime.now()))
        )
        today_solved_report = Count("pk", Q(responsed=True))
        reports_remaining = Count(
            "pk",
            Q(responsed=False,
                top_date_time__gte=current_timezone.localize(
                    datetime.datetime.now())
              )
        )
        today_new_report = Count("pk")
        today_report = Report.objects.filter(get_date_time__date=current_timezone.localize(datetime.datetime.today())).aggregate(
            today_not_solved_report=today_not_solved_report,
            today_solved_report=today_solved_report,
            reports_remaining=reports_remaining,
            today_new_report=today_new_report
        )
        agree_series = []
        not_agree_series = []
        dates_series = []
        min_date = Report.objects.aggregate(
            first_date=Min("get_date_time"))["first_date"]
        if(min_date is not None):
            midnight = datetime.time(0)
            range_date = datetime.datetime.combine(min_date.date(), midnight)
            agree_count = Count("pk", Q(agree=True))
            not_agree_count = Count("pk", Q(agree=False))
            while range_date <= datetime.datetime.today():
                next_day = range_date + relativedelta(days=1)
                day_counts = Report.objects.filter(response_date_time__range=(current_timezone.localize(
                    range_date), current_timezone.localize(next_day))).aggregate(agree_count=agree_count, not_agree_count=not_agree_count)
                agree_series.append(day_counts["agree_count"])
                not_agree_series.append(day_counts["not_agree_count"])
                dates_series.append(str(range_date))
                range_date = next_day

        context["panel"] = "Panel de control"
        context["data"] = today_report
        context["series"] = {"dates": dates_series,
                             "agree_series": agree_series, "not_agree_serise": not_agree_series}

        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
