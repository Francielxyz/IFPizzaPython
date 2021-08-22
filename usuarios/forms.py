from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CriarUsuario(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Verificar se email já existe no sistema
    def clean_email(self):
        emailDigitado = self.cleaned_data['email']
        if User.objects.filter(email=emailDigitado).exists():
            raise ValidationError("O email {} já está em uso.".format(emailDigitado))

        return emailDigitado
