from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClienteForm
from django.urls import reverse


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
