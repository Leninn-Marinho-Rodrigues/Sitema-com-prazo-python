from django.shortcuts import render
from .models import Tarefa
from datetime import date # Importamos a biblioteca de data

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('data_conclusao') # Busca todas as tarefas
    hoje = date.today() # Pega a data atual do sistema (ex: 2023-10-25)
    
    contexto = {
        'tarefas': tarefas,
        'hoje': hoje 
    }
    
    return render(request, 'index.html', contexto)