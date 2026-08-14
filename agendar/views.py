from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.contrib import messages

from .forms import ClienteForm, AgendamentoForm, HorarioForm
from .models import Cliente, HorarioModel, AgendamentoModel
from datetime import datetime, timedelta


def index(request):
    return HttpResponse("Hello, world.")


def thanks(request, nome):
    return render(request, "agendar/thanks.html", {"nome": nome})


def criarCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            # nome = form.cleaned_data["nome"]
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect("agendar:criarcliente")
            # return HttpResponseRedirect(reverse("agendar:thanks", args=(nome,)))
    else:
        form = ClienteForm()

    return render(request, "agendar/criarCliente.html", {"form": form})


def listar_clientes(request):
    clientes = Cliente.objects.all().order_by("nome")
    return render(request, "agendar/listarCliente.html", {"clientes": clientes})


def horario_cadastrar(request: HttpRequest):
    if request.method == "POST":
        formulario = HorarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Horário disponível cadastrado com sucesso!")
            return redirect("agendar:cadastrarHorario")
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados informados.')
    contexto = {"form": HorarioForm()}
    return render(request, "horarios/cadastrarHorario.html", contexto)


def agendamento_realizar(request: HttpRequest):
    if request.method == "POST":
        formulario = AgendamentoForm(request.POST)
        if formulario.is_valid():
            agendamento = formulario.save(commit=False)
            horario = agendamento.horario
            horario.livre = False
            horario.save()
            agendamento.save()
            messages.success(request, "Agendamento realizado com sucesso!")
            return redirect("agendar:realizarAgendamento")
        else:
            messages.error(request, 'Erro ao realizar o agendamento. Verifique os dados informados.')
    contexto = {"form": AgendamentoForm()}
    return render(request, "horarios/realizarAgendamento.html", contexto)

def agenda_horarios(request):
    numeroSemana = int(request.GET.get('semana',0))
    #Retorna a semana que está sendo visualizada pelo usuário. Semana atual = 0
    hoje = datetime.now().date()
    segunda = hoje - timedelta(days = hoje.weekday()) + timedelta(weeks = numeroSemana)

    horariosSemana = HorarioModel.objects.filter(data__range=[segunda,segunda + timedelta(days = 6)]
    ).select_related("agendamento__cliente").order_by('horario')
    #Realiza uma consulta no banco de dados retornando todos os horarios pertencentes a aquela semana


    diasSemana = [
        {'nome': 'SEGUNDA', 'data': segunda, 'horarios': []},
        {'nome': 'TERÇA', 'data': segunda + timedelta(days=1), 'horarios': []},
        {'nome': 'QUARTA', 'data': segunda + timedelta(days=2), 'horarios': []},
        {'nome': 'QUINTA', 'data': segunda + timedelta(days=3), 'horarios': []},
        {'nome': 'SEXTA', 'data': segunda + timedelta(days=4), 'horarios': []},
        {'nome': 'SÁBADO', 'data': segunda + timedelta(days=5), 'horarios': []},
        {'nome': 'DOMINGO', 'data': segunda + timedelta(days =6), 'horarios': []},
    ]

    for h in horariosSemana:
        numero_dia = h.data.weekday()
        diasSemana[numero_dia]['horarios'].append(h)
    
    contexto = {
        'dias_semana': diasSemana,
        'inicio_semana': segunda,
        'fim_semana' : segunda + timedelta(days = 6),
        'semana_atual': numeroSemana,
        'proxima_semana' : numeroSemana + 1,
        'semana_anterior' : numeroSemana -1,

    }
    return render(request,'horarios/homeHorarios.html',contexto)