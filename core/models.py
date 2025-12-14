from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    data_conclusao = models.DateField()  # Data para terminar a tarefa
    concluida = models.BooleanField(default=False) # Checkbox (True/False)

    def __str__(self):
        return self.titulo