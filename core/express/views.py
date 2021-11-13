from datetime import datetime, timedelta

from blitz_work.blitzcrud import BlitzCRUD
from core.express.models import (
    Attendant,
    Departament,
    KindRep,
    Report,
    Responce,
    Room,
    RoomState,
)
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse
from django.utils.timezone import now
import django_filters

# from django.shortcuts import render
from core.express.resources import ReportResource


class XeniaCRUD(BlitzCRUD):
    show_title = True
    show_caption = False
    caption_is_title = True
    extend_template = "base.html"
    template_name = "base_crud.html"
    table_template = "table.html"
    create_template = "create.html"
    update_template = "update.html"
    create_title = "Nuevo"
    delete_title = "Eliminar"
    update_title = "Editar"
    detail_title = "Detalle"
    paginate_by = 10
    dark_mode_switch_label = None
    delete_messages = {
        "success": "Operación completada",
        "error": "No fue posible completar la operación",
    }
    delete_text = "¿Desea eliminar de forma permanente los siguientes elementos?"
    crud_buttons = {
        "add": "Nuevo",
        "create": "Guardar",
        "details": "Detalle",
        "update": "Actualizar",
        "edit": "Editar",
        "delete": "Eliminar",
        "cancel": "Cancelar",
        "return": "Regresar",
        "search": "Buscar",
    }

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ReportCRUD(XeniaCRUD):
    model = Report
    form_template = "components/custom/ex_report_form.html"
    multiform_template = "components/custom/ex_report_form_multi.html"
    fields = [
        "report_number",
        "kind",
        "description",
        "executive",
        "attendant",
        "get_date_time",
        "top_date_time",
        "response_date_time",
        "solved",
        "responce",
    ]
    exclude = []
    include = {"departament": F("attendant__dpt__name_dpt")}
    # include = {"client_name": Concat(F("client_room__client__first_name"), Value(
    #     " "), F("client_room__client__last_name")),"room":F("client_room__room__number") , "departament": F("attendant__dpt__name_dpt")}
    # include = {"client_first_name":F("client_room__client__first_name"),"client_last_name":F("client_room__client__last_name")}
    # include_header = {"client_first_name": "Nombre Cliente", "client_last_name" : "Apellidos Cliente"}
    include_header = {"departament": "Departamento"}
    fields_priority = Report.get_fields_priority()


@login_required()
def get_report_xlsx(request):
    filename = f'Tabla_Reporte.xlsx'
    DATE_CHOICES = (("today", "Hoy"), ("last_10_days", "Últimos 10 días"))

    class DateRangeFilter(django_filters.DateRangeFilter):
        filters = {
            'today': lambda qs, name: qs.filter(**{
                '%s__year' % name: now().year,
                '%s__month' % name: now().month,
                '%s__day' % name: now().day
            }),
            "last_10_days": lambda qs, name: qs.filter(**{
                f"{name}__gte": now() - timedelta(10)
            })
        }

    class CustomFilter(django_filters.FilterSet):
        date_range = DateRangeFilter(field_name="get_date_time__date", choices=DATE_CHOICES)

        class Meta:
            model = Report
            fields = ["date_range"]

    queryset = CustomFilter(request.GET).qs
    file = ReportResource().export(queryset).export("xlsx")
    response = HttpResponse(
        file,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response


class RoomCRUD(XeniaCRUD):
    model = Room
    exclude = ["id"]
    form_exclude = []
    # include = {"client_first_name":F("client_room__client__first_name"),"client_last_name":F("client_room__client__last_name")}
    # include_header = {"client_first_name": "Nombre Cliente", "client_last_name" : "Apellidos Cliente"}
    # include_header = {"client_name": "Cliente"}


class RoomStateCRUD(XeniaCRUD):
    model = RoomState


class AttendantCRUD(XeniaCRUD):
    model = Attendant


class DepartamentCRUD(XeniaCRUD):
    model = Departament


class ResponceCRUD(XeniaCRUD):
    model = Responce


class KindCRUD(XeniaCRUD):
    model = KindRep
