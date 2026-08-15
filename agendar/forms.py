from django import forms
from .models import Cliente, HorarioModel, AgendamentoModel
from django.db.models import Q
from datetime import datetime

class HorarioForm(forms.ModelForm):
    class Meta:
        model = HorarioModel
        # model = TarefaModel
        fields = ["data", "horario"]
        widgets = {
            'data' : forms.DateInput(
                attrs = { 'type': 'date', }
            ),
            'horario' : forms.TimeInput(
                attrs = { 'type': 'time',}
            )

        }


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = AgendamentoModel
        fields = ["cliente", "horario"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        agora = datetime.now()
        hoje = agora.date()
        hora_atual = agora.time()
        self.fields["horario"].queryset = HorarioModel.objects.filter(
            livre=True
        ).filter(
            Q(data__gt=hoje) | Q(data=hoje, horario__gte=hora_atual)
        ).order_by("data", "horario")
        # Retorna apenas horários não agendados ainda.


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        # fields = ["cpf", "nome", "telefone"]
