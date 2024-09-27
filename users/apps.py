from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals # signals imported so that whenever the ready function is run, the signals will be imported...upon import action the signals will generate and get passed to create/save profiles of the users