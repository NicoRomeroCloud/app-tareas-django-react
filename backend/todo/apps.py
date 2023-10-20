from django.apps import AppConfig


# En resumen, este archivo de configuración específica
# de la aplicación "Todo" establece algunas configuraciones
# predeterminadas para la aplicación, como el tipo de campo
# de clave primaria a utilizar. También proporciona un nombre
# identificativo para la aplicación dentro del proyecto Django.
class TodoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo"
