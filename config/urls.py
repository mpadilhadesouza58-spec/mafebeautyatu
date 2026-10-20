
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import contato, categorias, promocoes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produtos/', include('produtos.urls')),
    path('contato/', contato, name='contato'),
    path('categorias/', categorias, name='categorias'),
    path('promocoes/', promocoes, name='promocoes'),
]