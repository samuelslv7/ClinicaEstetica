class HorarioForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['data','horario']