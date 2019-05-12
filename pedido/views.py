from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Product, Order
from pedido.forms import RegisterForm

# Create your views here.

def maxiapp(request):
    return render(request, 'pedido/index.html', {})

def loginview(request):
    url = "http://scrumreserva.pythonanywhere.com/admin"
    return redirect(url)

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(username=usuario,first_name=nombre,last_name=apellido, email=email, password=password_one, is_staff=True)
            u.save()
            return render(request, 'pedido/welcome.html', {})
        else:
            ctx = {'form':form}
            return render(request, 'pedido/register.html', ctx)
    ctx = {'form':form}
    return render(request, 'pedido/register.html', ctx)
