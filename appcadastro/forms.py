from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    confirmacao_senha = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirme sua senha"
    )

    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'telefone', 'email', 'data_nascimento', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        if senha != confirmacao_senha:
            raise forms.ValidationError("As senhas não correspondem.")

        return cleaned_data