from django import forms
from .models import Cliente, HorarioModel, AgendamentoModel
import re


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
        fields = ['nome', 'cpf', 'telefone']

        def clean_cpf(self):
            cpf = self.cleaned_data.get('cpf', '')
            cpf_numeros = re.sub(r'\D', '', cpf)

            if len(cpf_numeros) != 11:
                raise forms.ValidationError('O CPF deve conter exatamente 11 dígitos.')

            existe_outro = (
                Cliente.objects.filter(cpf=cpf_numeros)
                .exclude(pk=self.instance.pk)
                .exists()
            )

            if existe_outro:
                raise forms.ValidationError(
                    'Já existe outro cliente cadastrado com este CPF.'
                )

            return cpf_numeros
