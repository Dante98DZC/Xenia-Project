from blitz_work.blitzcrud import get_urls
from core.login.views import *
from core.main.views import UserCreate, UserManagement
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("", LoginFormView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("management/user/view/", UserManagement.as_view(), name="user_view"),
    path("management/user/create/", UserCreate.as_view(), name="user_create"),
]
