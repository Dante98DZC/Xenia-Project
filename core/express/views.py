from django.shortcuts import render
# Create your views here.
 
from core.express.models import Report
from blitz_work.blitzcrud import BlitzCRUD


class ReportCRUD(BlitzCRUD):
        show_title = True
        show_caption = False
        caption_is_title = True
        extend_template = "base.html"
        data = Report

    
        # def ExpressView(request):
        #     return render(request, 'express.html')