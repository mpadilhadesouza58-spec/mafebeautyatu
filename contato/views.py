from django.shortcuts import render, redirect
from .models import MensagemContato


def pagina_contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        assunto = request.POST.get('assunto', '').strip()
        mensagem = request.POST.get('mensagem', '').strip()

        if nome and email and assunto and mensagem:
            MensagemContato.objects.create(
                nome=nome,
                email=email,
                assunto=assunto,
                mensagem=mensagem
            )

            return redirect('/contato/?enviado=1')

    return render(request, 'contato.html', {
        'mensagem_enviada': request.GET.get('enviado') == '1'
    })