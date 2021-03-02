from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from core.api.serializers import TarefaSerializer
from core.models import Tarefa


class TarefasViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        usuario_logado = get_object_or_404(User, pk=self.request.user.id)
        return Tarefa.objects.filter(usuario=usuario_logado)

    def perform_create(self, serializer):
        usuario_logado = get_object_or_404(User, pk=self.request.user.id)
        serializer.save(usuario=usuario_logado)
