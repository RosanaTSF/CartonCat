from django.db import models
from django.core.files.storage import FileSystemStorage
from multiselectfield import MultiSelectField

# Definição das escolhas para detalhes médicos
DETALHES_MEDICOS_CHOICES = [
    ('VACINADO', 'Vacinado'),
    ('VERMIFUGADO', 'Vermifugado'),
    ('CASTRADO', 'Castrado'),
]

# Definição das escolhas para tipo de animal
TIPO_CHOICES = (
    ('Gato', 'Gato'),
)

# Configuração do sistema de armazenamento de arquivos
fs = FileSystemStorage(location='media/')

class Animal(models.Model):
    STATUS_CHOICES = [
        ('Disponível', 'disponivel'),
        ('Adotado', 'adotado'),
    ]
    SEXO_CHOICES = [
        ('Macho', 'Gato'),
        ('Fêmea', 'Gata'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Disponível')
    nome = models.CharField(max_length=30)
    gênero = models.CharField(max_length=10, choices=SEXO_CHOICES, default='Macho')
    cor = models.CharField(max_length=10)
    cuidados = MultiSelectField(choices=DETALHES_MEDICOS_CHOICES, max_length=50)
    idade = models.CharField(max_length=20)  # Adicionando o campo idade
    foto_animal = models.ImageField(upload_to='images/', storage=fs, blank=True)
    descricao = models.TextField(blank=True)  # O campo pode ser deixado em branco
    foto = models.ImageField(upload_to='fotos_gatos/', storage=fs, blank=True)  # Adicionando o campo foto

    def save(self, *args, **kwargs):
        # Preencher a descrição com base nos outros campos
        self.descricao = f"{self.nome}, com {self.idade} anos. Adora crianças e ama brincar ❤️. Está à procura de uma nova família. Ajude a encontrar um lar amoroso!"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome