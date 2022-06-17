from django.http import HttpResponse
from django.shortcuts import render
from .forms import PedidoFormulario, ProductoFormulario, UserFormulario
from .models import Carrito, Producto, Usuario

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def user_formulario(request):

    if request.method == 'POST':

        nuevo_user = UserFormulario(request.POST)

        if nuevo_user.is_valid():

            info = nuevo_user.cleaned_data

            mi_usuario = Usuario(nombre = info['nombre'],apellido = info['apellido'],edad = info['edad'])
            mi_usuario.save()

            return render(request, "AppCoder/userCreado.html",{'nombre': info['nombre'], 'apellido': info['apellido']})
    
    else:

        user_formulario = UserFormulario()
        
    return render(request, "AppCoder/userFormulario.html", {'miForm': user_formulario})


def producto_formulario(request):

    if request.method == 'POST':
        
        nuevo_producto = ProductoFormulario(request.POST)

        if nuevo_producto.is_valid():

            info = nuevo_producto.cleaned_data

            mi_producto = Producto(nombre = info['nombre'],categoria = info['categoria'],precio = info['precio'],stock = info['cantidad'])
            mi_producto.save()

            return render(request, "AppCoder/productoAgregado.html",{'nombre': info['nombre'], 'cantidad': info['cantidad']})
    
    else:

        producto_formulario = ProductoFormulario()

    return render(request, "AppCoder/productoFormulario.html", {'miForm': producto_formulario})

def pedido_formulario(request):

    if request.method == 'POST':
        
        nuevo_pedido = PedidoFormulario(request.POST)

        if nuevo_pedido.is_valid():

            info = nuevo_pedido.cleaned_data
            mi_pedido = Carrito(producto= info['producto'], cantidad= info['cantidad'])
            mi_pedido.save()

            return render(request, "AppCoder/pedidoCreado.html",{'producto': info['producto'], 'cantidad': info['cantidad'],'nombre': info['nombre']})
    
    else:

        pedido_formulario = PedidoFormulario()

    return render(request, "AppCoder/pedidoFormulario.html", {'miForm': pedido_formulario})


def busquedaUsuario(request):
        
    return render(request, 'AppCoder/busquedaUsuario.html')
    

def buscar(request):
    
    if request.GET['edad']:
        edad = request.GET['edad']
        users = Usuario.objects.filter(edad=edad)

        if users:

            return render(request, 'AppCoder/resultadoBusqueda.html', {'users':users, 'edad':edad})

        else:

            respuesta = 'No se encontraron usuarios'
            return render(request, 'AppCoder/busquedaUsuario.html', {'respuesta':respuesta})

    else:
        
        respuesta = 'Ingrese una edad'
        return render(request, 'AppCoder/busquedaUsuario.html', {'respuesta':respuesta})
    