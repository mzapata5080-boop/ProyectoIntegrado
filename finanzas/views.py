from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Proveedor
from .forms import ProveedorForm

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'finanzas/proveedor_list.html'
    context_object_name = 'proveedores'

class ProveedorCreateView(SuccessMessageMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'finanzas/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')
    success_message = "Proveedor registrado exitosamente."

class ProveedorUpdateView(SuccessMessageMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'finanzas/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')
    success_message = "Proveedor actualizado correctamente."

class ProveedorDeleteView(SuccessMessageMixin, DeleteView):
    model = Proveedor
    template_name = 'finanzas/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')
    success_message = "Proveedor eliminado del sistema."
