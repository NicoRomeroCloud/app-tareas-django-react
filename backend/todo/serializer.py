# Importamos las bibliotecas necesarias.
# serializers es parte de Django REST framework y
# se utiliza para definir cómo se deben serializar y
# deserializar los modelos de Django.
# También importamos el modelo Todo que será serializado.
from rest_framework import serializers
from .models import Todo


# Definimos una clase llamada TodoSerializer que hereda de
# serializers.ModelSerializer.
# Esto significa que estamos utilizando un serializador de
# modelo que simplifica la serialización de modelos de Django.
class TodoSerializer(serializers.ModelSerializer):

    # Dentro de la clase TodoSerializer, definimos una clase interna
    # Meta. En esta clase, especificamos cómo se debe serializar
    # el modelo Todo. Los atributos clave son:

    # model: Se establece en Todo, lo que indica que este
    # serializador se utiliza para el modelo Todo.

    # fields: Es una tupla que contiene los campos del
    # modelo que se deben serializar. En este caso, estamos
    # serializando los campos id, title, description y done del
    # modelo Todo.
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'done')
