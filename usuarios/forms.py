from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import Trabajador

class TrabajadorCrearForm(UserCreationForm):
    rol = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        empty_label="Seleccione un Rol",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta(UserCreationForm.Meta):
        model = Trabajador
        fields = ('username', 'nombre', 'apellido', 'email', 'rut', 'telefono', 'rol')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12.345.678-K'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            rol_seleccionado = self.cleaned_data.get('rol')
            if rol_seleccionado:
                user.groups.add(rol_seleccionado)
        return user


class TrabajadorEditarForm(UserChangeForm):
    password = None  # No se muestra el campo contraseña al editar para no borrar el hash
    rol = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Trabajador
        fields = ('username', 'nombre', 'apellido', 'email', 'rut', 'telefono', 'is_active', 'rol')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.groups.exists():
            self.fields['rol'].initial = self.instance.groups.first()

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user.groups.clear()
            rol_seleccionado = self.cleaned_data.get('rol')
            if rol_seleccionado:
                user.groups.add(rol_seleccionado)
        return user
    