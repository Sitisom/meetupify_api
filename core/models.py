from django.contrib.auth.models import AbstractUser
from django.db import models


class DefaultModel(models.Model):
    created_at = models.DateTimeField('Создано', auto_created=True)
    updated_at = models.DateTimeField('Обновлено', auto_now_add=True)


class User(AbstractUser):
    phone = models.CharField('Номер телефона', default='')
    friends = models.ManyToManyField('self')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
