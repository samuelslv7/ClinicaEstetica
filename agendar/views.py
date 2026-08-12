from django.shortcuts import render
from django.http import HttpResponse
from .forms import HorarioForm, AgendamentoForm
from .models import HorarioModel, AgendamentoModel

def index(request):
    return HttpResponse("Hello, world.")

def horario_cadastrar(request:HttpRequest):
    if request.method == "POST":
        formulario =  HorarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("horarios:home")
    contexto = {
        "form" : HorarioForm
    }
    return render(request,'horarios/cadastrarHorario.html',contexto)

def agendamento_realizar(request:HttpRequest):
    if request.method == "POST":
        formulario = AgendamentoForm(request.POST)
        if formulario.is_valid():
            agendamento = formulario.save(commit = False )
            horario = agendamento.horario
            horario.livre = False 
            horario.save()
            agendamento.save()
            return redirect("agendamento:home")
    contexto = {
        "form" : AgendamentoForm()
    }
    return render(request, 'agendamento/realizarAgendamento.html',contexto)