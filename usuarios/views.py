from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Trabajador
from .forms import TrabajadorCrearForm, TrabajadorEditarForm

# Create your views here.

class EsGerenteMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Gerencia').exists()

class TrabajadorListView(LoginRequiredMixin, EsGerenteMixin, ListView):
    model = Trabajador
    template_name = 'usuarios/trabajador_list.html'
    context_object_name = 'trabajadores'

class TrabajadorCreateView(LoginRequiredMixin, EsGerenteMixin, CreateView):
    model = Trabajador
    form_class = TrabajadorCrearForm
    template_name = 'usuarios/trabajador_form.html'
    success_url = reverse_lazy('trabajador_list')

    def form_valid(self, form):
        messages.success(self.request, "Trabajador registrado exitosamente.")
        return super().form_valid(form)

class TrabajadorUpdateView(LoginRequiredMixin, EsGerenteMixin, UpdateView):
    model = Trabajador
    form_class = TrabajadorEditarForm
    template_name = 'usuarios/trabajador_form.html'
    success_url = reverse_lazy('trabajador_list')

    def form_valid(self, form):
        messages.success(self.request, "Datos del trabajador actualizados correctamente.")
        return super().form_valid(form)

class TrabajadorDeleteView(LoginRequiredMixin, EsGerenteMixin, DeleteView):
    model = Trabajador
    template_name = 'usuarios/trabajador_confirm_delete.html'
    success_url = reverse_lazy('trabajador_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Trabajador eliminado del sistema.")
        return super().delete(request, *args, **kwargs)