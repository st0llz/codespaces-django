from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Se um usuario nao logado faz uma request relacionado a index esta funcao o redireciona para o login.
@login_required
def index(request):
    return render(request, 'index.html')

# View da página de cadastro
def registrar_usuario(request):
    return render(request, 'paginaCadastro.html')

# View da página de login
def login_view(request):
    return render(request, 'login.html', {'title': 'Login'})

