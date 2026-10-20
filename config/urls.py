

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial pública
    path('', views.home, name='home'),

    # Dashboard administrativo
    path('dashboard/', views.dashboard, name='dashboard'),

    # Aplicativo de produtos
    path('produtos/', include('produtos.urls')),

    # Aplicativo de usuários
    path('usuarios/', include('usuario.urls')),

    # Páginas públicas
    path('contato/', views.contato, name='contato'),
    path('categorias/', views.categorias, name='categorias'),
    path('promocoes/', views.promocoes, name='promocoes'),
]
