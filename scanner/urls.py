from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="home"),
    path("settings/", views.settings , name="settings"),
    path("setting_data/", views.setting_data , name="setting_data"),
    path("upload_excel/", views.upload_excel , name="upload_excel"),
    path("hapus_data_emiten/", views.hapus_data_emiten , name="hapus_data_emiten"),



]