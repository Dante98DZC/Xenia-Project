"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.main.views import DashboardView
from core.express.views import *

from django.urls import path,include

from django.contrib import admin
from blitz_work.urls import urlpatterns

urlpatterns = [
    path('',include(urlpatterns)),
    path('login/', include('core.login.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # path('express/report', ReportCRUD, name='api_report'),
    #el segundo parametro de get_urls(ReportCRUD,"api_report") es un nompre para el crud es opcional pq blitz lo coje del modelo
    path('express/', include('core.express.urls')),
    
    
]

