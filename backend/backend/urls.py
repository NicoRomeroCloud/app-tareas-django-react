"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Se importa las bibliotecas y módulos necesarios de Django.
# admin se utiliza para acceder al panel de administración de Django,
# path se utiliza para definir rutas URL, include se utiliza para
# incluir otras rutas en este archivo, todo.views se importa para
# acceder a las vistas definidas en el archivo views.py, y routers
# se importa de Django REST framework para configurar enrutadores.
from django.contrib import admin
from django.urls import path, include
from todo import views
from rest_framework import routers

# Se crea un enrutador utilizando routers.DefaultRouter().
# Luego, se registra la vista TodoView en el enrutador con
# el nombre tasks. Esto configura las rutas URL para las
# operaciones CRUD relacionadas con las tareas utilizando el enrutador.
router = routers.DefaultRouter()
router.register(r'tasks', views.TodoView, 'task')

# Configuramos las rutas URL de la aplicación:

# path("admin/", admin.site.urls):
# Esta ruta se utiliza para acceder al panel de
# administración de Django. Cuando los usuarios navegan
# a /admin/, se redirigen al panel de administración de Django.


# path('api/', include(router.urls)):
# Esta ruta se utiliza para incluir las rutas generadas
# por el enrutador router. Todas las rutas relacionadas
# con las tareas se agrupan bajo /api/.
# Por ejemplo, para acceder a la lista de tareas,
# la URL sería /api/tasks/.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls))
]
