
from django.contrib.auth.decorators import login_required
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


def promocoes(request):
    return render(request, 'promocoes.html')


@login_required(login_url='/usuarios/login/')
def dashboard(request):
    total_produtos = Produto.objects.count()

    return render(request, 'dashboard.html', {
        'total_produtos': total_produtos,
    })
