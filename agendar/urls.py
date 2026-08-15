from django.urls import path

from . import views

app_name = "agendar"
urlpatterns = [
    path("", views.index, name="index"),
    path("clientes/", views.listar_clientes, name="listarclientes"),
    path("clientes/novo", views.criarCliente, name="criarcliente"),
    path("thanks/<str:nome>", views.thanks, name="thanks"),
    path("clientes/<str:cliente_cpf>/editar", views.editar_cliente, name="editarcliente"),
    path("clientes/<str:cliente_cpf>/deletar/",views.deletar_cliente,name="deletarcliente"),
    path("horarios/",views.agenda_horarios,name="agenda"),
    path("horarios/cadastrarHorario",views.horario_cadastrar,name="cadastrarHorario"),
    path("horarios/realizarAgendamento",views.agendamento_realizar,name="realizarAgendamento"),
    path("horarios/cancelarHorario",views.horario_cancelar,name="cancelarHorario")

]
