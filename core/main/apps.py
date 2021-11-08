from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.main"

    def ready(self):
        from core.main.report_task import start

        start()
