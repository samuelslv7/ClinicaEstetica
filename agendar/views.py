from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.contrib import messages

from .forms import ClienteForm, AgendamentoForm, HorarioForm
from .models import Cliente, HorarioModel, AgendamentoModel


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


def editar_cliente(request, cliente_cpf):
    cliente = get_object_or_404(Cliente, cpf=cliente_cpf)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados do cliente atualizados com sucesso!")
            return redirect("agendar:listarclientes")
    else:
        form = ClienteForm(instance=cliente)

    return render(request, "agendar/editarcliente.html", {"form": form, "cliente": cliente})
