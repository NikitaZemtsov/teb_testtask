from django.apps import AppConfig
from django.urls import reverse_lazy
# from django.contrib.sites.models import Site

class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'


def get_login_url():
    # print(Site.objects.get_current().domain)
    print(reverse_lazy('login'))
    return 'http://127.0.0.1:8000/login'
