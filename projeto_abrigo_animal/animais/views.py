from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AnimalForm
from .models import Animal
from .utils import get_client_ip, get_geolocation
import folium

# ----------------------------------------------------------------------- HOME

def home(request):
    """
    View para a página inicial. Cria uma instância do formulário de Animal e
    recupera todos os objetos Animal do banco de dados para exibir.
    """
    form = AnimalForm()
    animais = Animal.objects.all()
    return render(request, 'home.html', {'animais': animais, 'form': form})

# ----------------------------------------------------------------------- MAP

def map_view(request, lat=-23.9613, lon=-46.391):
    """
    Cria um mapa com Folium, definindo marcadores na posição padrão e na posição fornecida.
    Salva o mapa gerado no template map.html para exibição.
    """
    mapa = folium.Map(location=[-22.449, -48.6388], zoom_start=6.5)
    folium.Marker(location=[-21.1775000, -47], icon=folium.Icon(popup="Star Icon", color='purple')).add_to(mapa)
    folium.Marker(location=[float(lat), float(lon)], icon=folium.Icon(color='orange')).add_to(mapa)
    mapa.save('animais/templates/map.html')
    return render(request, 'map.html')

# ----------------------------------------------------------------------- DETALHES

def detalhes(request, id):
    """
    Exibe os detalhes de um animal específico, incluindo um mapa de localização baseado no IP do usuário.
    """
    ip = get_client_ip(request)
    ip = '177.100.236.65'  # Para testes, define um IP fixo.
    lat, lon = get_geolocation(ip)

    animal = get_object_or_404(Animal, id=id)
    map_view(request, lat, lon)
    return render(request, 'detalhes.html', {'animal': animal})

# ----------------------------------------------------------------------- CADASTRO ANIMAL

def cadastro(request):
    """
    View para cadastro de novos animais. Processa o formulário e salva no banco se for válido.
    """
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnimalForm()
    return render(request, 'cadastro.html', {'form': form})

# ----------------------------------------------------------------------- REGISTER (EXEMPLO DE CADASTRO DE USUÁRIO)

from django.contrib.auth.forms import UserCreationForm

def register(request):
    """
    View para registro de novos usuários usando UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})