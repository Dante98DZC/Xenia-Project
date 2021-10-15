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
from core.express.views import ExecutiveCRUD, ReportCRUD, ClientsCRUD, RoomCRUD, ClientRoomCRUD,RoomStateCRUD

from django.urls import path,include

from django.contrib import admin
from blitz_work.blitzcrud import get_urls
from blitz_work.urls import urlpatterns

urlpatterns = [
    path('',include(urlpatterns)),
    path('login/', LoginFormView.as_view() , name='login'),
    path('admin/', admin.site.urls),
    path('index/', MainView, name='index'),
    # path('express/report', ReportCRUD, name='ex_report'),
    #el segundo parametro de get_urls(ReportCRUD,"ex_report") es un nompre para el crud es opcional pq blitz lo coje del modelo
    path('express/report/', include(get_urls(ReportCRUD,"ex_report"))),
    path('express/client/', include(get_urls(ClientsCRUD,"ex_client"))),
    path('express/executive/', include(get_urls(ExecutiveCRUD,"ex_executive"))),
    path('express/room/', include(get_urls(RoomCRUD,"ex_room"))),
    path('express/client_room/', include(get_urls(ClientRoomCRUD,"ex_client_room"))),
    path('express/room_state/', include(get_urls(RoomStateCRUD,"ex_room_state"))),
    
]

