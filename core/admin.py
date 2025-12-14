from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_conclusao', 'concluida')

admin.site.register(Tarefa, TarefaAdmin)