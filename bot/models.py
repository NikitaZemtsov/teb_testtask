from django.db import models
from django.contrib.auth import get_user_model


class TelegramUser(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='telegram_user')

    chat_id = models.CharField(
        max_length=20)
    phone = models.CharField(max_length=20)
    photo = models.URLField(default='https://photoshablon.com/_ph/44/2/52953599.jpg?1680956368')

    def __str__(self) -> str:
        return str(self.chat_id)

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user
        self.save()

    def set_data(self, **kwargs):
        self.photo = kwargs['photo_url']
        self.phone = kwargs['phone_number']
        self.save()
