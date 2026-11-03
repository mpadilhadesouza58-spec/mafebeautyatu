from django.shortcuts import render, redirect
from .models import Categoria


def lista_categorias(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

        if nome and descricao:
            Categoria.objects.create(
                nome=nome,
                descricao=descricao
            )

            return redirect('/categorias/')

    categorias_cadastradas = Categoria.objects.all()

    return render(request, 'categorias.html', {
        'categorias_cadastradas': categorias_cadastradas
    })