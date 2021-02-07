from django.contrib import admin

from .models import Tarefa


class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data_add', 'usuario')
    list_display_links = ('id', 'descricao')
    search_fields = 'descricao',
    list_filter = ('feita',)
    list_per_page = 10


admin.site.register(Tarefa, TarefaAdmin)
