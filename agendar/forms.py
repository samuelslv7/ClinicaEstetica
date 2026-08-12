from django import forms
from .models import Cliente


'''class HorarioForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ["data", "horario"]'''


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        # fields = ["cpf", "nome", "telefone"]
