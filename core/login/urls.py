from blitz_work.blitzcrud import get_urls
from core.login.views import *
from core.main.views import UserCreate, UserDelete, UserManagement, UserUpdate
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("", LoginFormView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("management/user/view/", UserManagement.as_view(), name="user_view"),
    path("management/user/create/", UserCreate.as_view(), name="user_create"),
    path("management/user/update/<path:pk>/", UserUpdate.as_view(), name="user_update"),
    path("management/user/delete/<path:pk>/", UserDelete.as_view(), name="user_delete"),
]
