from django.urls import path, include
from rest_framework import routers

from rest_framework.authtoken import views

from core.api.viewsets import TarefasViewSet

router = routers.SimpleRouter()
router.register('tarefas', TarefasViewSet, basename='tarefa')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.obtain_auth_token)
]
