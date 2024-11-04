from django.shortcuts import render, get_object_or_404, redirect  # Funções de atalho do Django para renderizar templates, buscar objetos e redirecionar.
from .forms import AnimalForm  # Importa o formulário do modelo Animal.
from .models import Animal  # Importa o modelo Animal.
from django.http import HttpResponse, HttpResponseRedirect  # Importa classes para respostas HTTP.
import folium  # Biblioteca para criação de mapas.
import requests  # Biblioteca para realizar requisições HTTP.
import ipaddress  # Biblioteca para manipular e validar endereços IP.

# ----------------------------------------------------------------------- HOME

def home(request):
    """
    View para a página inicial. Cria uma instância do formulário de Animal e
    recupera todos os objetos Animal do banco de dados para exibir.
    """
    form = AnimalForm()  # Instancia o formulário de Animal para uso na página.
    animais = Animal.objects.all()  # Busca todos os animais no banco de dados.
    return render(request, 'home.html', {'animais': animais, 'form': form})  # Renderiza o template home.html com o contexto de animais e formulário.

# ----------------------------------------------------------------------- MAP

def get_client_ip(request):
    """
    Função auxiliar para obter o endereço IP do cliente a partir do request.
    Verifica se há um IP via proxy (HTTP_X_FORWARDED_FOR) ou usa o REMOTE_ADDR.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # Pega o primeiro IP da lista de IPs.
    else:
        ip = request.META.get('REMOTE_ADDR')  # Usa o IP direto do cliente.
    return ip

def get_client_ipv4(request):
    """
    Obtém o endereço IPv4 do cliente se disponível. Se for um IPv6, retorna None.
    """
    ip = get_client_ip(request)
    try:
        ip_obj = ipaddress.ip_address(ip)  # Valida o endereço IP.
        if isinstance(ip_obj, ipaddress.IPv4Address):
            return str(ip_obj)  # Retorna o IPv4 como string.
        else:
            return None  # Retorna None para IPv6 ou se o IP não é tratável.
    except ValueError:
        return None  # Em caso de IP inválido ou não parseável.

def get_geolocation(ip_address):
    """
    Obtém a geolocalização de um IP usando uma API externa.
    Retorna a latitude e longitude associadas ao IP.
    """
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url)  # Faz a requisição para a API de geolocalização.
    data = response.json()  # Obtém a resposta JSON com os dados de localização.

    latitude = data['lat']  # Extrai a latitude.
    longitude = data['lon']  # Extrai a longitude.

    return latitude, longitude  # Retorna a latitude e longitude como tupla.

def map_view(request, lat=-23.9613, lon=-46.391):
    """
    Cria um mapa com Folium, definindo marcadores na posição padrão e na posição fornecida.
    Salva o mapa gerado no template map.html para exibição.
    """
    mapa = folium.Map(location=[-22.449, -48.6388], zoom_start=6.5)  # Mapa centralizado em uma posição padrão.
    folium.Marker(location=[-21.1775000, -47], icon=folium.Icon(popup="Star Icon", color='purple')).add_to(mapa)  # Adiciona um marcador fixo.
    folium.Marker(location=[float(lat), float(lon)], icon=folium.Icon(color='orange')).add_to(mapa)  # Adiciona um marcador na posição especificada.
    mapa.save('animais/templates/map.html')  # Salva o mapa em um arquivo HTML.
    return render(request, 'map.html')  # Renderiza o template map.html.

# ----------------------------------------------------------------------- DETALHES

def detalhes(request, id):
    """
    Exibe os detalhes de um animal específico, incluindo um mapa de localização baseado no IP do usuário.
    """
    ip = get_client_ip(request)  # Obtém o IP do cliente.
    ip = '177.100.236.65'  # Para testes, define um IP fixo.
    lat, lon = get_geolocation(ip)  # Obtém latitude e longitude a partir do IP.

    animal = get_object_or_404(Animal, id=id)  # Busca o objeto Animal pelo id, ou retorna erro 404 se não existir.
    map_view(request, lat, lon)  # Cria o mapa com a localização do cliente.
    return render(request, 'detalhes.html', {'animal': animal})  # Renderiza o template detalhes.html com o contexto do animal.

# ----------------------------------------------------------------------- CADASTRO ANIMAL

def cadastro(request):
    """
    View para cadastro de novos animais. Processa o formulário e salva no banco se for válido.
    """
    if request.method == 'POST':  # Verifica se o método é POST para submissão do formulário.
        form = AnimalForm(request.POST, request.FILES)  # Cria o formulário com os dados enviados.
        if form.is_valid():  # Valida o formulário.
            form.save()  # Salva o formulário no banco de dados.
            return HttpResponseRedirect('/')  # Redireciona para a página inicial após o cadastro.
    else:
        form = AnimalForm()  # Cria uma nova instância do formulário em caso de GET.
    return render(request, 'cadastro.html', {'form': form})  # Renderiza o template cadastro_animal.html com o formulário.

# ----------------------------------------------------------------------- REGISTER (EXEMPLO DE CADASTRO DE USUÁRIO)

from django.contrib.auth.forms import UserCreationForm  # Formulário padrão para criação de usuários do Django.

def register(request):
    """
    View para registro de novos usuários usando UserCreationForm.
    """
    if request.method == 'POST':  # Verifica se o método é POST para submissão do formulário.
        form = UserCreationForm(request.POST)  # Cria o formulário com os dados enviados.
        if form.is_valid():  # Verifica se o formulário é válido.
            form.save()  # Salva o novo usuário no banco de dados.
            return HttpResponseRedirect('/')  # Redireciona após o registro.
    else:
        form = UserCreationForm()  # Instancia o formulário em caso de GET.
    return render(request, 'register.html', {'form': form})  # Renderiza o template register.html com o formulário.
