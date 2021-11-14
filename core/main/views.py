import datetime

from core.express.models import Report
from core.express.views import XeniaCRUD
from core.main.models import NotificationUser
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import ExpressionWrapper, F
from django.db.models.aggregates import Count, Min
from django.db.models.fields import DurationField
from django.db.models.functions import Coalesce
from django.db.models.query_utils import Q
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, TemplateView,
                                  UpdateView)
from django.views.generic.detail import DetailView


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
            "pk",
            Q(
                solved=False,
                top_date_time__lte=timezone.now(),
            ),
        )
        today_solved_report = Count("pk", Q(solved=True))
        reports_remaining = Count(
            "pk",
            Q(
                solved=False,
                top_date_time__gte=timezone.now(),
            ),
        )
        today_new_report = Coalesce(Count("pk"), 0)

        today_report = Report.objects.filter(
            get_date_time__date=timezone.now().today()
        ).aggregate(
            today_not_solved_report=today_not_solved_report,
            today_solved_report=today_solved_report,
            reports_remaining=reports_remaining,
            today_new_report=today_new_report,
        )
        agree_series = []
        not_agree_series = []
        dates_series = []
        min_date = Report.objects.filter(solved=True).aggregate(
            first_date=Min("response_date_time")
        )["first_date"]
        agree_count = Count("pk", Q(agree=True))
        not_agree_count = Count("pk", Q(agree=False))
        if min_date is not None:
            midnight = datetime.time(0)
            range_date = datetime.datetime.combine(min_date.date(), midnight)
            while range_date <= timezone.now().today():
                next_day = range_date + relativedelta(days=1)
                day_counts = Report.objects.filter(
                    response_date_time__range=(
                        range_date,
                        next_day,
                    ),
                    solved=True,
                ).aggregate(agree_count=agree_count, not_agree_count=not_agree_count)
                agree_series.append(day_counts["agree_count"])
                not_agree_series.append(day_counts["not_agree_count"])
                dates_series.append(str(range_date))
                range_date = next_day

        current = ExpressionWrapper(
            timezone.now() - F("get_date_time"),
            output_field=DurationField(),
        )
        duration = ExpressionWrapper(
            F("top_date_time") - F("get_date_time"), output_field=DurationField()
        )
        remaining_reports = (
            Report.objects.filter(
                Q(
                    solved=False,
                    top_date_time__gte=timezone.now(),
                )
            )
            .select_related("room", "kind")
            .annotate(time_to_end=duration, current_time=current)
        )
        not_solved = Count("pk", Q(solved=False))
        value_donut = Report.objects.aggregate(
            not_solved=not_solved, solved=today_solved_report
        )
        context["panel"] = "Panel de control"
        context["data"] = today_report
        context["series"] = {
            "dates": dates_series,
            "agree_series": agree_series,
            "not_agree_serise": not_agree_series,
            "not_solved": value_donut["not_solved"],
            "solved": value_donut["solved"],
        }
        context["reports"] = remaining_reports

        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class OnlyView(XeniaCRUD):
    def get(self, request, *args, **kwargs):
        return self.list_view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["GET"])

    def put(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["GET"])

    def delete(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["GET"])

    def get_crud_url(self):
        return {}


class UserManagement(OnlyView):
    model = User
    table_template = "user_management.html"
    template_name = "management_crud.html"
    exclude = ["password", "date_joined", "is_active", "is_staff"]
    fields_priority = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "last_login",
    ]


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "is_superuser",
        ]


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = "user_create.html"
    success_url = reverse_lazy("user_view")


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = "user_update.html"
    success_url = reverse_lazy("user_view")


class UserDetail(DetailView):
    model = User
    template_name = "user_detail.html"


class UserDelete(DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy("user_view")


def delete_notification(request, pk):
    if request.method == "POST":
        NotificationUser.objects.filter(pk=pk).delete()
        return HttpResponse("")
    return HttpResponseNotAllowed(["POST"])


def delete_all_notification(request):
    if request.method == "POST":
        NotificationUser.objects.filter(user=request.user).delete()
        return HttpResponse("")
    return HttpResponseNotAllowed(["POST"])
