from django.shortcuts import render

# Importamos la clase viewsets de Django REST framework.
# Los viewsets son una forma de definir vistas basadas en
# clases que simplifican la creación de vistas CRUD para modelos
# de Django.
from rest_framework import viewsets

# Importamos el serializador TodoSerializer y el modelo
# Todo desde los archivos correspondientes en el mismo directorio.
from .serializer import TodoSerializer
from .models import Todo


# Definimos una clase llamada TodoView que hereda de
# viewsets.ModelViewSet. Esto significa que estamos utilizando un
# viewset proporcionado por Django REST framework para manejar las
# operaciones CRUD relacionadas con el modelo Todo.
class TodoView(viewsets.ModelViewSet):
    # Dentro de la clase TodoView, configuramos los
    # siguientes atributos:
    # serializer_class: Se establece en TodoSerializer,
    # lo que indica que este viewset utilizará ese serializador
    # para manejar la serialización y deserialización de datos
    # relacionados con el modelo Todo.
    # queryset: Se establece en Todo.objects.all(),
    # lo que significa que este viewset trabajará con todas las
    # instancias del modelo Todo en la base de datos.
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
