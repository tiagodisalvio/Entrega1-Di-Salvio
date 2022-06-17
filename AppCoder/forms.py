from django import forms

class UserFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()

class ProductoFormulario(forms.Form):

    nombre = forms.CharField()
    categoria = forms.CharField()
    precio = forms.IntegerField()
    cantidad = forms.IntegerField()

class PedidoFormulario(forms.Form):

    producto = forms.CharField()
    cantidad = forms.IntegerField()
    nombre = forms.CharField()