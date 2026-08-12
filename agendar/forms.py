
from django import forms
from .models import HorarioModel, AgendamentoModel

class HorarioForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['data','horario']

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = AgendamentoModel
        fields = ['cliente', 'horario']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['horario'].queryset = HorarioModel.objects.filter(livre=True).order_by('data', 'horario')
        # Retorna apenas horários não agendados ainda.