from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    is_staff = models.BooleanField(default=True)
    list_display = ['nome', 'cpf', 'email', 'telefone', 'data_nascimento']
    search_fields = ['nome', 'cpf', 'email']
    list_filter = ['data_nascimento']

admin.site.register(Usuario, UsuarioAdmin)