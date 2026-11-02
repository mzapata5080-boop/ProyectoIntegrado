from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Trabajador
from .forms import TrabajadorCrearForm, TrabajadorEditarForm

# Lista de Trabajadores
class TrabajadorListView(ListView):
    model = Trabajador
    template_name = 'usuarios/trabajador_list.html'
    context_object_name = 'trabajadores'

# Crear Trabajador
class TrabajadorCreateView(CreateView):
    model = Trabajador
    form_class = TrabajadorCrearForm
    template_name = 'usuarios/trabajador_form.html'
    success_url = reverse_lazy('trabajador_list')

# Editar Trabajador
class TrabajadorUpdateView(UpdateView):
    model = Trabajador
    form_class = TrabajadorEditarForm
    template_name = 'usuarios/trabajador_form.html'
    success_url = reverse_lazy('trabajador_list')

# Eliminar Trabajador
class TrabajadorDeleteView(DeleteView):
    model = Trabajador
    template_name = 'usuarios/trabajador_confirm_delete.html'
    success_url = reverse_lazy('trabajador_list')