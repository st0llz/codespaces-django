from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome Completo"
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(r'^\d{11}$', 'O CPF deve conter exatamente 11 dígitos.')
        ],
        verbose_name="CPF"
    )
    telefone = models.CharField(
        max_length=15,
        blank=True,
        validators=[
            RegexValidator(r'^\+?\d{9,15}$', 'O telefone deve conter entre 9 e 15 dígitos. Inclua o código do país se necessário.')
        ],
        verbose_name="Telefone"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento"
    )
    senha = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(8, 'A senha deve ter no mínimo 8 caracteres.')
        ],
        verbose_name="Senha"
    )

    def set_senha(self, raw_password):
        self.senha = make_password(raw_password)
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['nome']
        