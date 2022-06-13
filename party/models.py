from uuid import uuid4

from django.db import models

# Create your models here.
from django.utils import timezone

from core.models import User, DefaultModel


class Category(DefaultModel):
    title = models.CharField('Название', max_length=128)
    icon = models.FileField('Иконка', upload_to='icons/category/')
    order = models.PositiveSmallIntegerField('Порядок', default=999)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order', )


class Group(DefaultModel):
    title = models.CharField('Название', max_length=128)
    users = models.ManyToManyField(User, 'related_groups', through='ParticipantsThroughModel',
                                   verbose_name='Пользователи')
    date = models.DateTimeField('Время встречи', null=True, default=timezone.now)
    link = models.UUIDField('Хэш доступа', default=uuid4)
    full_amount = models.PositiveSmallIntegerField('Сумма на группу', default=0)
    is_active = models.BooleanField('Активно?', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Record(DefaultModel):
    title = models.CharField('Наименование', max_length=64, blank=True, default='')
    category = models.ForeignKey(Category, models.SET_NULL, 'records', null=True, verbose_name='Категория')
    amount = models.PositiveSmallIntegerField('Сумма', default=0)

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name = 'Запись траты'
        verbose_name_plural = 'Записи трат'


class ParticipantsThroughModel(DefaultModel):
    user = models.ForeignKey(User, models.CASCADE, 'spending', verbose_name='Пользователь')
    group = models.ForeignKey(Group, models.CASCADE, 'spending', verbose_name='Группа')
    records = models.ManyToManyField(Record, blank=True, verbose_name='Расходы')

    # amount = models.PositiveSmallIntegerField('Потраченная сумма', default=0)
    want_to = models.BooleanField('Собирается идти на встречу?', default=False)
    came = models.BooleanField('Пришел на встречу?', default=False)

    class Meta:
        verbose_name = 'Участие пользователей'


class Invite(DefaultModel):
    sender = models.ForeignKey(User, models.CASCADE, 'sent_invites')
    receiver = models.ForeignKey(User, models.CASCADE, 'received_invites')
    group = models.ForeignKey(Group, models.CASCADE, 'invites')

    is_active = models.BooleanField('Активно?', default=True)

    class Meta:
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашения'

