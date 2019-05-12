from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    usuario = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput())
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput())
    apellido = forms.CharField(label="Apellido", widget=forms.TextInput())
    email = forms.CharField(label="Correo Electronico", widget=forms.TextInput())
    password_one = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False), min_length=8)
    password_two = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(render_value=False))

    def clean_usuario(self):
        username = self.cleaned_data['usuario']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("El nombre de usuario ya esta Ocupado")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("Email ya se encuentra Registrado, ingrese otro")

    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']

        if(password_one == password_two):
            pass
        else:
            raise forms.ValidationError("Las contraseñas no coinciden")