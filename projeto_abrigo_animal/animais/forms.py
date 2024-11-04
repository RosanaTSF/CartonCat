from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['status', 'nome', 'sexo', 'cor', 'detalhes_medicos', 'foto_animal']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Escolha um nome de usuário', 'class': 'form-control'}),
        }
