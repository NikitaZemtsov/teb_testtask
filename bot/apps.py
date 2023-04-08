from django.apps import AppConfig
from django.urls import reverse_lazy
# from django.contrib.sites.models import Site

class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'


def get_login_url():
    return 'https://web-production-c739.up.railway.app/login/'
