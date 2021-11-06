import datetime

from core.express.models import Report
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Count, Sum
from django.db.models.query_utils import Q
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


# Create your views here.
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
            top_date_time__lte=datetime.datetime.now())
        )
        today_solved_report = Count("pk", Q(responsed=True))
        reports_remaining = Count(
            "pk",
            Q(responsed=False,
                top_date_time__gte=datetime.datetime.now()
            )
        )
        today_new_report = Count("pk")
        today_report = Report.objects.filter(get_date_time__date=datetime.datetime.today()).aggregate(
            today_not_solved_report=today_not_solved_report,
            today_solved_report=today_solved_report,
            reports_remaining=reports_remaining,
            today_new_report=today_new_report
        )
        context["panel"] = "Panel de control"
        context["data"] = today_report

        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
