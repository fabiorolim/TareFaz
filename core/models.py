from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    descricao = models.CharField(max_length=50, blank=False,
                                 verbose_name='descrição')
    feita = models.BooleanField(default=False, verbose_name='Feita')
    data_add = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
