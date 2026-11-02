import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Proveedor

def validar_rut_chileno(rut_str):
    rut_limpio = re.sub(r'[^0-9kK]', '', str(rut_str)).upper()
    if len(rut_limpio) < 8 or len(rut_limpio) > 9:
        raise ValidationError('El RUT debe tener entre 8 y 9 caracteres.')
    
    cuerpo, dv = rut_limpio[:-1], rut_limpio[-1]
    suma = 0
    multiplicador = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplicador
        multiplicador = 2 if multiplicador == 9 else multiplicador + 1
    
    resto = suma % 11
    dv_esperado = 11 - resto
    dv_calculado = '0' if dv_esperado == 11 else ('K' if dv_esperado == 10 else str(dv_esperado))
    
    if dv != dv_calculado:
        raise ValidationError('El RUT ingresado no es válido (dígito verificador incorrecto).')

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rut', 'razon_social', 'cuenta_bancaria']
        labels = {
            'rut': 'RUT del Proveedor',
            'razon_social': 'Razón Social',
            'cuenta_bancaria': 'Cuenta Bancaria / Banco',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '76.999.888-1'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Distribuidora Ejemplo SpA'}),
            'cuenta_bancaria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BancoEstado - 123456'}),
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not rut:
            return rut
        
        validar_rut_chileno(rut)
        
        instance = self.instance
        if Proveedor.objects.filter(rut=rut).exclude(pk=instance.pk).exists():
            raise forms.ValidationError("Este RUT ya se encuentra registrado en el sistema.")

        return rut