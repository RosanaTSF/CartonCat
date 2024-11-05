from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # Importa as views de autenticação do Django

urlpatterns = [
    path('', views.home, name='home'),
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('map/', views.map_view, name='map'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Adiciona a URL de login
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)