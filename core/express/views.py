from django.db.models.query_utils import Q
# from django.shortcuts import render

from django.db.models import Count, F, Value
from django.db.models.functions import Concat
from core.express.models import *
from blitz_work.blitzcrud import BlitzCRUD


class XeniaCRUD(BlitzCRUD):
    show_title = True
    show_caption = False
    caption_is_title = True
    extend_template = "base.html"
    template_name = "base_crud.html"
    table_template = "table.html"
    create_template = "create.html"
    create_title = "Nuevo"
    delete_title = "Eliminar"
    update_title = "Editar"
    detail_title = "Detalle"
    paginate_by = 10
    dark_mode_switch_label = None
    delete_messages = {"success": "Operación completada",
                       "error": "No fue posible completar la operación"}
    delete_text = "¿Desea eliminar de forma permanente los siguientes elementos?"
    crud_buttons = {"add": "Nuevo", "create": "Guardar", "details": "Detalle",
                    "update": "Actualizar", "edit": "Editar", "delete": "Eliminar", "cancel": "Cancelar",
                    "return": "Regresar", "search": "Buscar"}



class ReportCRUD(XeniaCRUD):
    model = Report
    form_template = "components/custom/ex_report_form.html"
    fields= ["report_number","kind", "description",
                       "executive", "attendant", "get_date_time", "com_date_time",
                       "response_date_time", "responsed", "responce"]
    exclude = ['']
    include = {"client_name": Concat(F("client_room__client__first_name"), Value(
        " "), F("client_room__client__last_name"))}
    # include = {"client_first_name":F("client_room__client__first_name"),"client_last_name":F("client_room__client__last_name")}
    # include_header = {"client_first_name": "Nombre Cliente", "client_last_name" : "Apellidos Cliente"}
    include_header = {"client_name": "Cliente"}
    fields_priority = ["report_number", "client_name", "client_room", "kind", "description",
                       "executive", "attendant", "get_date_time", "com_date_time",
                       "response_date_time", "responsed", "responce"]



class ExecutiveCRUD(XeniaCRUD):
    model = Executive


class RoomCRUD(XeniaCRUD):
    model = Room
    exclude = ['']
    form_exclude = []
    # include = {"client_first_name":F("client_room__client__first_name"),"client_last_name":F("client_room__client__last_name")}
    # include_header = {"client_first_name": "Nombre Cliente", "client_last_name" : "Apellidos Cliente"}
    include_header = {"client_name": "Cliente"}


class ClientRoomCRUD(XeniaCRUD):
    model = ClientRoom


class RoomStateCRUD(XeniaCRUD):
    model = RoomState


class ClientsCRUD(XeniaCRUD):
    form_exclude = []
    model = Client


class ExecutiveCRUD(XeniaCRUD):
    model = Executive
    

class ObservCRUD(XeniaCRUD):
    model = Observ

class AttendantCRUD(XeniaCRUD):
    model = Attendant
    
class DepartamentCRUD(XeniaCRUD):
    model = Departament

class ResponceCRUD(XeniaCRUD):
    model = Responce
    
class KindCRUD(XeniaCRUD):
    model = KindRep