from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm

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

def cadastrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_senha(form.cleaned_data["senha"])  # Hash da senha
            usuario.save()
            return redirect('pagina_de_sucesso')  # Altere para a página de destino após o cadastro
    else:
        form = UsuarioForm()

    return render(request, 'paginaCadastro.html', {'form': form})