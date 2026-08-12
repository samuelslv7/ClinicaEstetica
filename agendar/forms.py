from django import forms
from .models import Cliente, HorarioModel, AgendamentoModel


class HorarioForm(forms.ModelForm):
    class Meta:
        model = HorarioModel
        # model = TarefaModel
        fields = ["data", "horario"]


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = AgendamentoModel
        fields = ["cliente", "horario"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["horario"].queryset = HorarioModel.objects.filter(
            livre=True
        ).order_by("data", "horario")
        # Retorna apenas horários não agendados ainda.


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        # fields = ["cpf", "nome", "telefone"]
