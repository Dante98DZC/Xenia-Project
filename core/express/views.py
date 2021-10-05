# from django.db.models.aggregates import Count
from django.shortcuts import render
# Create your views here.

# from django.db.models.aggregates import Count
from django.db.models import Count, F, Value
from core.express.models import Report
from core.express.models import Client
from blitz_work.blitzcrud import BlitzCRUD


class ReportCRUD(BlitzCRUD):
        model = Report
        show_title = True
        show_caption = False
        caption_is_title = True
        extend_template = "base.html"
        paginate_by = 10
        exclude = ['']
        include = {"client_name":F("client__client__first_name")}
        include_header = {"client_name": "Nombre Cliente"}
        
        
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
        # data era antes q dejaba meter queryset tambien despues me arrepenti y deje q fuese para modelos solamente
        #data = Report 
        model = Client