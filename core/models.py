from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class DefaultModel(models.Model):
    created_at = models.DateTimeField('Создано', auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField('Обновлено', auto_now_add=True, )

    class Meta:
        abstract = True


class User(AbstractUser):
    phone = models.CharField('Номер телефона', default='', max_length=15)
    friends = models.ManyToManyField('self')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
