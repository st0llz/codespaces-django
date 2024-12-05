from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import UsuarioForm


# Função para verificar se o usuário é admin
def is_admin_user(user):
    return user.is_staff


# Para qualquer pagina restrita à Usuarios logados, usar "@login_required"
# Para qualquer pagina restrita à Amin, usar "@user_passes_test(is_admin_user)"


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

# View do historico do usuario.
# O template precisa ser ajustado para preencher a tabela dinamicamente.
def historico_usuario(request):
    pedidos = Pedido.objects.filter(usuario=request.user)  # Exemplo de consulta
    context = {
        'pedidos': pedidos
    }
    return render(request, 'historicoUsuario.html', context)

# View da tabela de produtos para o admin.
# O template precisa ser ajustado para preencher a tabela dinamicamente.
@user_passes_test(is_admin_user)
def tabelaAdm_view(request):
    produtos = Produto.objects.all()  # Exemplo de consulta ao banco de dados
    context = {'produtos': produtos}
    return render(request, 'tabelaAdm.html', context)