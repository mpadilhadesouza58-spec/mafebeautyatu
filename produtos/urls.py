from django.urls import path
from .views import (
    ProdutoListView,
    ProdutoDetailView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView,
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_lista'),
    path('novo/', ProdutoCreateView.as_view(), name='produto_novo'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='produto_detalhe'),
    path('<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_editar'),
    path('<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='produto_excluir'),
]