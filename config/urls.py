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
from core.main.views import MainView
from core.login.views import LoginFormView
from core.express.views import ExecutiveCRUD,AttendantCRUD,DepartamentCRUD, ReportCRUD, ClientsCRUD, RoomCRUD, ClientRoomCRUD,RoomStateCRUD,ObservCRUD,ResponceCRUD,KindCRUD

from django.urls import path,include

from django.contrib import admin
from blitz_work.blitzcrud import get_urls
from blitz_work.urls import urlpatterns

urlpatterns = [
    path('',include(urlpatterns)),
    path('login/', LoginFormView.as_view() , name='login'),
    path('admin/', admin.site.urls),
    path('index/', MainView, name='index'),
    # path('express/report', ReportCRUD, name='api_report'),
    #el segundo parametro de get_urls(ReportCRUD,"api_report") es un nompre para el crud es opcional pq blitz lo coje del modelo
    path('api/report/', include(get_urls(ReportCRUD,"api_report"))),
    path('api/client/', include(get_urls(ClientsCRUD,"api_client"))),
    path('api/executive/', include(get_urls(ExecutiveCRUD,"api_executive"))),
    path('api/room/', include(get_urls(RoomCRUD,"api_room"))),
    path('api/client_room/', include(get_urls(ClientRoomCRUD,"api_client_room"))),
    path('api/room_state/', include(get_urls(RoomStateCRUD,"api_room_state"))),
    path('api/observ/', include(get_urls(ObservCRUD,"api_observ"))),
    path('api/attendant/', include(get_urls(AttendantCRUD,"api_attendant"))),
    path('api/departament/', include(get_urls(DepartamentCRUD,"api_departament"))),
    path('api/responce/', include(get_urls(ResponceCRUD,"api_responce"))),
    path('api/kindrep/', include(get_urls(KindCRUD,"api_kindrep"))),
    
    
    
]

