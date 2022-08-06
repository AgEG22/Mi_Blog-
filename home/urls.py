from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # el name=index es darle un nombre a esa url.
]

## Lo que esta entre comilla vacio es la ruta a la que yo quiero que aparezca el "Hola mundo".

## Aqui configuramos que rutas van a mostrar la vista, definida por la funcion index. 