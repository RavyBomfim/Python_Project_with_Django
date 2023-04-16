from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
# from django.urls import reverse

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        user = User.objects.filter(username=username)
        emailin = User.objects.filter(email=email)

        if user.exists() and emailin.exists():
            messages.add_message(request, constants.ERROR, 'Usuário e email já existem.')
            return redirect('/usuarios/cadastro')
            ''' Importando a função reverse de django.urls, eu posso substituir o trecho anterior e todos os trechos semelhantes pelo seguinte comando:'''
            # return redirect(reverse('cadastro'))
        
        elif user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe.')
            return redirect('/usuarios/cadastro')
            # return redirect(reverse('cadastro'))
        
        elif emailin.exists():
            messages.add_message(request, constants.ERROR, 'Este email já existe.')
            return redirect('/usuarios/cadastro')
            # return redirect(reverse('cadastro'))
        
        elif not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect('/usuarios/cadastro')
            # return redirect(reverse('cadastro'))
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso.')
        
        return redirect('/usuarios/login')
        # return redirect(reverse('login'))

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            return redirect('/usuarios/login')
            # return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('/eventos/novo_evento/')