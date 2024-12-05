from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import UsuarioForm




# View da página de login
def login_view(request):
    return render(request, 'login.html', {'title': 'Login'})

# View da página de cadastro com redirecionamento para a pagina de sucesso.
def cadastrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_senha(form.cleaned_data["senha"])  # Hash da senha
            usuario.save()
            return redirect('/')  # Altere para a página de destino após o cadastro
    else:
        form = UsuarioForm()

    return render(request, 'paginaCadastro.html', {'form': form})
