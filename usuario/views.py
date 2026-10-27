from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def cadastro(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          email = request.POST.get('email')
          password = request.POST.get('password1')
          password2 = request.POST.get('password2')

          if password != password2:
               messages.error(request, 'As senhas não são iguais.')
               return redirect('usuario:cadastro')

          if User.objects.filter(username=username).exists():
               messages.error(request, 'Esse nome de usuário já existe.')
               return redirect('usuario:cadastro')

          User.objects.create_user(
               username=username,
               email=email,
               password=password
          )

          messages.success(request, 'Conta criada com sucesso!')
          return redirect('usuario:login')

     return render(request, 'usuario/cadastro.html')

@login_required
def dashboard_admin(request):
    return render(request, 'usuarios/aluno/dashboard.html')