from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    tel = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
