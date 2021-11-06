from blitz_work.blitzcrud import get_urls
from django.urls import include, path

from core.express.views import *

urlpatterns = [
    path("api/report/", include(get_urls(ReportCRUD, "api_report"))),
    path("api/client/", include(get_urls(ClientsCRUD, "api_client"))),
    path("api/executive/", include(get_urls(ExecutiveCRUD, "api_executive"))),
    path("api/room/", include(get_urls(RoomCRUD, "api_room"))),
    path("api/client_room/", include(get_urls(ClientRoomCRUD, "api_client_room"))),
    path("api/room_state/", include(get_urls(RoomStateCRUD, "api_room_state"))),
    path("api/observ/", include(get_urls(ObservCRUD, "api_observ"))),
    path("api/attendant/", include(get_urls(AttendantCRUD, "api_attendant"))),
    path("api/departament/", include(get_urls(DepartamentCRUD, "api_departament"))),
    path("api/responce/", include(get_urls(ResponceCRUD, "api_responce"))),
    path("api/kindrep/", include(get_urls(KindCRUD, "api_kindrep"))),
]
