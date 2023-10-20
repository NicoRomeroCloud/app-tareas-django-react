# Importamos la biblioteca models de Django,
# que se utiliza para definir modelos de base de datos.
from django.db import models


# Definimos una clase llamada Todo que hereda de models.Model.
# Esto crea un modelo de base de datos en Django llamado Todo.
class Todo(models.Model):
    # Creamos un campo de texto title y description en el modelo Todo
    # utilizando models.CharField.
    # Este campo se utiliza para almacenar
    # el título de la tarea y tiene una longitud máxima de 130 caracteres.
    title = models.CharField(max_length=130)
    description = models.CharField(max_length=130)

    # Creamos un campo booleano done en el modelo Todo que se
    # utiliza para indicar si la tarea está completa o no.
    # Por defecto, se establece en False, lo que significa
    # que una tarea se considera incompleta al crearla.
    done = models.BooleanField(default=False)


# Definimos un método __str__ que devuelve una representación
# de cadena del objeto Todo. En este caso, devuelve el título
# de la tarea. Esto es útil para representar objetos Todo de
# manera legible cuando se utilizan en el administrador de Django
# u otras partes de la aplicación.

    def __str__(self):
        return self.title
