from turtle import update
from unicodedata import category
from venv import create
from django.db import models
from django.conf import settings 
# Create your models here.

class Post(models.Model):  # models: modulo que estoy importando. Model: la calse base. Todo esto esta heredando la calse Post.
    #Asi se crea los campos:
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add: lo que hace es rellenar el campo created_at cuando se realiza una creacion. 
    update_at = models.DateTimeField(auto_now=True) 
    # esto hace que se rellene cuando se realiza una modificacion.
    title =  models.CharField(max_length=125) 
    slug = models.SlugField(max_length=125, unique=True) #es la URL.
    content = models.TextField()
    author =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #aqui llamamos al usuario que definimmos en el settings que se encuentra en el archivo base.py. Todo esto para construir el campo autor.
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True) ##Esto hace que este campo sea obligatorio.
    # imagen = models.ImageField(upload_to='images/', blank=True, null=True)
    #campo cuando se quiere agregar imagen, este se sube a la carpeta static, media y que son subidas por el usuario.  
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    nombre = models.CharField(max_length=225)



## Estos modelos luego se traduce en tablas en la base de datos con estos campos, estos campos se define como me define django como: models.(DateTimeField--->nombre del campo) 

# FINALIZADO ESTO TENGO QUE CREAR EL ARCHIVO DE MIGRACION PARA QUE ESTO FGURE EN LA BASE DE DATOS. Y ESTE MOSTRARA LAS MODIFICACIONES QUE YO CREE. Y CON python manage.py migrate, ESTOS CAMBIOS SE ESCRIBE EN LA BASE DE DATOS

# Luego esto es llevado al archivo admin.py de la app blog para que sea visualizado. 