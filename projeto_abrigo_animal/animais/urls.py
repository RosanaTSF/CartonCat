# urls.py
from django.urls import path  # Importa a função path para definir rotas.
from . import views  # Importa as views do aplicativo atual.
from django.conf import settings  # Importa as configurações do projeto, especialmente para verificar se está em modo DEBUG.
from django.conf.urls.static import static  # Importa a função para servir arquivos estáticos em desenvolvimento.

# Definindo as URLs do aplicativo
urlpatterns = [
    path('', views.home, name='home'),  # URL para a página inicial, chama a função 'home' na view.
    
    # URL para a página de detalhes de um animal específico, identificada pelo 'id' do animal.
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),  
    
    # URL para a página de cadastro de animais, chama a função 'cadastro' na view.
    path('cadastro/', views.cadastro, name='cadastro'),  
    
    # URL para a página do mapa, chama a função 'map_view' na view.
    path('map/', views.map_view, name='map'),  
    
    # URL para a página de registro de usuários, chama a função 'register' na view.
    path('register/', views.register, name='register'),  
]

# Configuração de URLs de mídia para servir arquivos de mídia em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve arquivos de mídia durante o desenvolvimento.