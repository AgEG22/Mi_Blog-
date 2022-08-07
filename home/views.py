from django.shortcuts import render, HttpResponse
from . import views   

# Create your views here. Yo aca creo mis vistas. 

def index(request):     
    return HttpResponse('Hola mundo, comenzemos a trabajar.') ## Esta en la funcion que me crea la vista

## que me muestra lo que yo quiera en un adetermidad ruta.    

##Aqui se crea la vista, con la funcion index.
## El HttResponse es un objeto que contiene la respusta segun la ruta especificada qeu el usario queire visitar. Para este caso la respuesta a la ruta diseñada es "Hola mundo" 
## El request es el pedido.. 