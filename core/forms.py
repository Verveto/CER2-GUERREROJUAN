from django import forms
from .models import Proyecto

class FormularioProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'estudiante', 'email', 'tema', 'descripcion']