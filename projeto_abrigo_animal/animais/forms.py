from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['status', 'nome', 'sexo', 'cor', 'detalhes_medicos', 'foto_animal']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'placeholder': 'Escolha um nome de usuário', 'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'}),
            'detalhes_medicos': forms.Textarea(attrs={'class': 'form-control'}),
            'foto_animal': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome.isalpha():
            raise forms.ValidationError('O nome deve conter apenas letras.')
        return nome