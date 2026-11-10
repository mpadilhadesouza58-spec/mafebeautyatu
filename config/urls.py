
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import contato, categorias, promocoes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produtos/', include('produtos.urls')),
    path('contato/', contato, name='contato'),
    path('promocoes/', promocoes, name='promocoes'),
    path('categorias/', categorias, name='categorias'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('categorias/', include('categorias.urls')),
    path('login/', LoginView.as_view(
        template_name='usuario/login.html'), name='login'),
    path('usuario/', include('usuario.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
