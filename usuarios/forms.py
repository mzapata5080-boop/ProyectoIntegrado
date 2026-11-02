from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Trabajador

class TrabajadorCrearForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Trabajador
        fields = ('username', 'first_name', 'last_name', 'email', 'rut', 'telefono')
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'rut': 'RUT',
            'telefono': 'Teléfono',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_email',
                'placeholder': 'ejemplo@correo.cl',
                'autocomplete': 'off'
            }),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password1' in self.fields:
            self.fields['password1'].label = "Contraseña"
            self.fields['password1'].help_text = (
                "<ul>"
                "<li>La contraseña no puede ser muy similar a tu información personal.</li>"
                "<li>Debe contener al menos 8 caracteres.</li>"
                "<li>No puede ser una contraseña común.</li>"
                "<li>No puede ser enteramente numérica.</li>"
                "</ul>"
            )
        if 'password2' in self.fields:
            self.fields['password2'].label = "Confirmación de contraseña"
            self.fields['password2'].help_text = "Ingresa la misma contraseña anterior para verificar."


class TrabajadorEditarForm(UserChangeForm):
    password = None  

    class Meta:
        model = Trabajador
        fields = ('username', 'first_name', 'last_name', 'email', 'rut', 'telefono', 'is_active')
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'rut': 'RUT',
            'telefono': 'Teléfono',
            'is_active': 'Estado Activo',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_email'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }