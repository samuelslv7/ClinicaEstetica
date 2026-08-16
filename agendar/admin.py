from django.contrib import admin
from .models import Cliente, AgendamentoModel, HorarioModel

admin.site.register(Cliente)
admin.site.register(AgendamentoModel)
admin.site.register(HorarioModel)
