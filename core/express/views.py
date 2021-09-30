from django.shortcuts import render
# Create your views here.
 
from core.express.models import Report
from core.express.models import Client
from blitz_work.blitzcrud import BlitzCRUD


class ReportCRUD(BlitzCRUD):
        show_title = True
        show_caption = False
        caption_is_title = True
        extend_template = "base.html"
        # data era antes q dejaba meter queryset tambien despues me arrepenti y deje q fuese para modelos solamente
        #data = Report 
        model = Report
    
        # def ExpressView(request):
        #     return render(request, 'express.html')
        
class ClientsCRUD(BlitzCRUD):
        show_title = True
        show_caption = False
        caption_is_title = True
        extend_template = "base.html"
        # data era antes q dejaba meter queryset tambien despues me arrepenti y deje q fuese para modelos solamente
        #data = Report 
        model = Client