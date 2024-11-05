from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import AnimalForm, GatoForm
from .models import Animal
from .utils import get_client_ip, get_geolocation
import folium

# ----------------------------------------------------------------------- HOME

def home(request):
    form = AnimalForm()
    animais = Animal.objects.all()
    return render(request, 'home.html', {'animais': animais, 'form': form})

# ----------------------------------------------------------------------- MAP

def map_view(request, lat=-23.9613, lon=-46.391):
    mapa = folium.Map(location=[-22.449, -48.6388], zoom_start=6.5)
    folium.Marker(location=[-21.1775000, -47], icon=folium.Icon(popup="Star Icon", color='purple')).add_to(mapa)
    folium.Marker(location=[float(lat), float(lon)], icon=folium.Icon(color='orange')).add_to(mapa)
    mapa.save('animais/templates/map.html')
    return render(request, 'map.html')

# ----------------------------------------------------------------------- DETALHES

def detalhes(request, id):
    ip = get_client_ip(request)
    ip = '177.100.236.65'  # Para testes, define um IP fixo.
    lat, lon = get_geolocation(ip)

    animal = get_object_or_404(Animal, id=id)
    map_view(request, lat, lon)
    return render(request, 'detalhes.html', {'animal': animal})

# ----------------------------------------------------------------------- CADASTRO ANIMAL

def cadastro(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet Cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = AnimalForm()
    return render(request, 'cadastro.html', {'form': form})

# ----------------------------------------------------------------------- CADASTRO GATO

def cadastro_gato(request):
    if request.method == 'POST':
        form = GatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gato cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = GatoForm()
    return render(request, 'cadastro_gato.html', {'form': form})

# ----------------------------------------------------------------------- REGISTER (EXEMPLO DE CADASTRO DE USUÁRIO)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro realizado com sucesso! Você já pode fazer login.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})