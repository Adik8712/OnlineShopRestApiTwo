from django.apps import AppConfig


class SupportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.support'
    verbose_name = "Поддержка"

    def ready(self) -> None:
        import apps.support.signals