# type:ignore
from django.apps import AppConfig


class TAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 't_app'
    verbose_name = ('t_app')

    def ready(self):
        import t_app.signals