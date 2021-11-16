from blitz_work.blitzcrud import get_urls
from core.login.views import *
from core.main.views import (
    UserCreate,
    UserDelete,
    UserDetail,
    UserManagement,
    UserUpdate,
    delete_all_notification,
    delete_notification,
    pdf_view,
)
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("", LoginFormView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("management/user/view/", UserManagement.as_view(), name="user_view"),
    path("management/user/create/", UserCreate.as_view(), name="user_create"),
    path("management/user/update/<path:pk>/", UserUpdate.as_view(), name="user_update"),
    path("management/user/detail/<path:pk>/", UserDetail.as_view(), name="user_detail"),
    path("management/user/delete/<path:pk>/", UserDelete.as_view(), name="user_delete"),
    path("notification/<path:pk>/", delete_notification, name="notification_delete"),
    path("notification/", delete_all_notification, name="notification_delete_all"),
    path("docs/", pdf_view, name="docs_view"),
]
