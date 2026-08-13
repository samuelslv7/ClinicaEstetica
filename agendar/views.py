from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .forms import ClienteForm, AgendamentoForm, HorarioForm
from django.urls import reverse

from .models import HorarioModel, AgendamentoModel


def index(request):
    return HttpResponse("Hello, world.")


def thanks(request, nome):
    return render(request, "agendar/thanks.html", {"nome": nome})
    return HttpResponse(f"Obrigado {nome}!")


def criarCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            form.save()
            return HttpResponseRedirect(reverse("agendar:thanks", args=(nome,)))
    else:
        form = ClienteForm()

    return render(request, "agendar/criarCliente.html", {"form": form})


def horario_cadastrar(request: HttpRequest):
    if request.method == "POST":
        formulario = HorarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("horarios:home")
    contexto = {"form": HorarioForm}
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
            return redirect("agendamento:home")
    contexto = {"form": AgendamentoForm()}
    return render(request, "agendamento/realizarAgendamento.html", contexto)
