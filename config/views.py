from django.shortcuts import render
from produtos.models import Produto


def home(request):
    produtos = Produto.objects.all()

    return render(request, 'index.html', {
        'produtos': produtos
    })


def contato(request):
    return render(request, 'contato.html')


def categorias(request):
    return render(request, 'categorias.html')