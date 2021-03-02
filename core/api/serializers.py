from core.models import Tarefa

from rest_framework import serializers


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
        read_only_fields = ['usuario']
