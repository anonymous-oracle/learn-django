from django.apps import AppConfig


class BlogConfig(AppConfig): # this is the config class for the blog app
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog' # referred by this name in the settings.py file in the apps list
