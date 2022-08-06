from django.shortcuts import render, HttpResponse
from . import views   
# Create your views here.

def index(request):     
    return HttpResponse('Hola mundo') ## Esta en la funcion que me crea la vista
                                      ## que me muestra lo que yo quiera en un adetermidad ruta.    

##Aqui se crea la vista, con la funcion index.
