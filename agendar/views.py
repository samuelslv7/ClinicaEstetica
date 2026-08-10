from django.shortcuts import render
from django.http import HttpResponse


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