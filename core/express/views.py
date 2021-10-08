from django.shortcuts import render

from django.db.models import Count, F, Value
from django.db.models.functions import Concat
from core.express.models import Report
from core.express.models import Client
from blitz_work.blitzcrud import BlitzCRUD


class ReportCRUD(BlitzCRUD):
        
        # def __init__(self, **kwargs):
        #         super().__init__(**kwargs)
        #         self.__fields = ["report_number","client_first_name","client_last_name","client_room",
        #                          "executive","attendant","kind","description","get_date_time","com_date_time",
        #                          "response_date_time","responsed","responce"]
        model = Report
        show_title = True
        show_caption = False
        caption_is_title = True
        extend_template = "base.html"
        template_name = "base_crud.html"
        table_template = "table.html"
        paginate_by = 10
        exclude = ['']
        # include = {"client_name":Concat(F("client_room__client__first_name"),Value(" "),F("client_room__client__last_name"))}
        include = {"client_first_name":F("client_room__client__first_name"),"client_last_name":F("client_room__client__last_name")}
        include_header = {"client_first_name": "Nombre Cliente", "client_last_name" : "Apellidos Cliente"}
        
        dark_mode_switch_label = None
        delete_messages = {"success": "Operación completada", "error": "No fue posible completar la operación"}
        create_title = "Nuevo Reporte"
        delete_title = "Eliminar Reporte"
        update_title = "Editar Reporte"
        detail_title = "Detalle del Reporte"
        delete_text = "¿Desea eliminar de forma permanente los siguientes elementos?"
        crud_buttons = {"add": "Nuevo", "create": "Crear", "details": "Detalle",
                        "update": "Actualizar", "edit": "Editar", "delete": "Eliminar", "cancel": "Cancelar",
                        "return": "Regresar", "search": "Buscar"}
        
class ClientsCRUD(BlitzCRUD):
        show_title = True
        show_caption = False
        caption_is_title = True
        extend_template = "base.html"
        model = Client