from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from .forms import RegistroUserCreationForm
from django.contrib.auth.models import Group
from .models import GestorPedidos
from .models import Producto

# Create your views here.

def realizar_pedido(request):
    if request.method == 'POST':
        total = int(request.POST.get('total'))  
        pedido = GestorPedidos.objects.create(Total=total, estado='P')  
        return redirect('compra')

    return redirect('Catalogo')

def home(request):

    return render(request,'core/Principal.html')

def compra(request):
    return render(request, 'core/compra.html')    

def Catalogo(request):
    productos = Producto.objects.all()  
    return render(request, 'core/Catalogo.html', {'productos': productos}) 

def Formulario(request):

    return render(request,'core/Formulario.html')  

def Registrarse(request):
    data = {
        'form': RegistroUserCreationForm()      
    }   

    if request.method == 'POST':
            Formulario = RegistroUserCreationForm(data=request.POST)
            if Formulario.is_valid():
                user = Formulario.save()

                grupo_clientes = Group.objects.get(name='Clientes')
                user.groups.add(grupo_clientes)

                usuario_autenticado = authenticate(username=Formulario.cleaned_data["username"], password=Formulario.cleaned_data["password1"])
                login(request, usuario_autenticado)
                return redirect(to='home')
            else:
                data['form'] = Formulario
            

    return render(request,'registration/Registrarse.html', data)    

@login_required
def IniciarSesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'core/Iniciar Sesion.html')       

def salir(request):
    logout(request)
    return redirect("home")
