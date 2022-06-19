from django.urls import path
from .views import buscar, busquedaUsuario, inicio, pedido_formulario, producto_formulario, user_formulario



urlpatterns = [
    path('', inicio, name='inicio'),
    path('userFormulario/', user_formulario, name='user_formulario'),
    path('productoFormulario/', producto_formulario, name='producto_formulario'),
    path('pedidoFormulario/', pedido_formulario, name='pedido_formulario'),
    path('busquedaUsuario/', busquedaUsuario, name='busqueda_usuario'),
    path('buscar/', buscar),
]
