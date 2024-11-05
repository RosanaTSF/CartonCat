from django.db import models
from multiselectfield import MultiSelectField

# Definição das escolhas para detalhes médicos
DETALHES_MEDICOS_CHOICES = [
    ('VACINADO', 'Vacinado'),
    ('VERMIFUGADO', 'Vermifugado'),
    ('CASTRADO', 'Castrado'),
]

# Definição das escolhas para gênero do animal
SEXO_CHOICES = [
    ('Gato', 'Gato'),
    ('Gata', 'Gata'),
]

class Animal(models.Model):
    STATUS_CHOICES = [
        ('Disponível', 'disponível'),
        ('Adotado', 'adotado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Disponível')
    nome = models.CharField(max_length=30)
    gênero = models.CharField(max_length=10, choices=SEXO_CHOICES, default='Gato')
    cor = models.CharField(max_length=10)
    cuidados = MultiSelectField(choices=DETALHES_MEDICOS_CHOICES, max_length=50)
    foto = models.ImageField(upload_to='fotos_gatos/', blank=True)  # Adicionando o campo foto

    def __str__(self):
        return self.nome

class Adocao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome