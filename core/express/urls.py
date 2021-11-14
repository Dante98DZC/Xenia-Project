from blitz_work.blitzcrud import get_urls
from core.express.views import *
from django.urls import include, path

urlpatterns = [
    path(
        "api/report/",
        include(
            get_urls(ReportCRUD, "api_report"),
        ),
    ),
    path("api/room/", include(get_urls(RoomCRUD, "api_room"))),
    path("api/room_state/", include(get_urls(RoomStateCRUD, "api_room_state"))),
    path("api/attendant/", include(get_urls(AttendantCRUD, "api_attendant"))),
    path("api/departament/", include(get_urls(DepartamentCRUD, "api_departament"))),
    path("api/responce/", include(get_urls(ResponceCRUD, "api_responce"))),
    path("api/kindrep/", include(get_urls(KindCRUD, "api_kindrep"))),
]
