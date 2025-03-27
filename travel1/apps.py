from django.apps import AppConfig


class Travel1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'travel1'
    # def ready(self):
    #     import travel1.signals