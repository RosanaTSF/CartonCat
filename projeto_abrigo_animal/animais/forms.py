from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['status', 'nome', 'cor', 'cuidados']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'placeholder': 'Escolha um nome de usuário', 'class': 'form-control'}),
            'cor': forms.Select(attrs={'class': 'form-control'}),
            'cuidados': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome.isalpha():
            raise forms.ValidationError('O nome deve conter apenas letras.')
        return nome

class GatoForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'cor', 'gênero', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do Gatinho', 'class': 'form-control'}),
            'cor': forms.Select(attrs={'class': 'form-control'}),
            'gênero': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome.isalpha():
            raise forms.ValidationError('O nome deve conter apenas letras.')
        return nome