from django.urls import path
from .views import (
    TrabajadorListView,
    TrabajadorCreateView,
    TrabajadorUpdateView,
    TrabajadorDeleteView
)

urlpatterns = [
    path('', TrabajadorListView.as_view(), name='trabajador_list'),
    path('crear/', TrabajadorCreateView.as_view(), name='trabajador_create'),
    path('<int:pk>/editar/', TrabajadorUpdateView.as_view(), name='trabajador_update'),
    path('<int:pk>/eliminar/', TrabajadorDeleteView.as_view(), name='trabajador_delete'),
]