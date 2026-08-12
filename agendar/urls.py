from django.urls import path

from . import views

app_name = "agendar"
urlpatterns = [
    path("", views.index, name="index"),
    path("criarcliente/", views.criarCliente, name="criarcliente"),
    path("thanks/<str:nome>", views.thanks, name="thanks"),
]
