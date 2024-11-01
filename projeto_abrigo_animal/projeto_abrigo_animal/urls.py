"""
Configuração de URLs para o projeto `projeto_abrigo_animal`.

A lista `urlpatterns` direciona URLs para as views apropriadas. Para mais informações, veja:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Exemplos:
Views baseadas em funções
    1. Adicione um import:  from my_app import views
    2. Adicione uma URL para `urlpatterns`:  path('', views.home, name='home')
Views baseadas em classes
    1. Adicione um import:  from other_app.views import Home
    2. Adicione uma URL para `urlpatterns`:  path('', Home.as_view(), name='home')
Incluindo outro arquivo de URL
    1. Importe a função `include`: from django.urls import include, path
    2. Adicione uma URL para `urlpatterns`:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para acessar o painel de administração
    path('', include('animais.urls')),  # Inclui URLs do app 'animais' na raiz do site
    path('usuarios/', include('usuarios.urls')),  # Inclui URLs do app 'usuarios' na rota '/usuarios/'
]

# Adiciona configuração para servir arquivos de mídia apenas em modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
