from django.db import models


class Cliente(models.Model):
    cpf = models.CharField("CPF", max_length=11, primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=9)

    def __str__(self):
        return self.nome + " " + self.cpf
        
class HorarioModel(models.Model):
    data = models.DateField()
    horario =  models.TimeField()
    livre = models.BooleanField(default = True)
    def __str__(self):
        return f"{self.data} {self.horario}"
