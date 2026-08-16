from django.db import models


class Cliente(models.Model):
    cpf = models.CharField("CPF", max_length=11, unique=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.nome}"


class HorarioModel(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    livre = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.data} {self.horario}"


class AgendamentoModel(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="agendamento"
    )
    horario = models.OneToOneField(
        HorarioModel, on_delete=models.CASCADE, related_name="agendamento"
    )
