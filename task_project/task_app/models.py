from datetime import datetime

from django.db import models

from django.utils.translation import gettext_lazy as _


class BShop(models.Model):
    """Модель барбершопа"""
    name = models.CharField(
        max_length=20,
        verbose_name=_('Название'),
    )
    address = models.CharField(
        max_length=40,
        verbose_name=_('Адрес'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Барбершоп')
        verbose_name_plural = _('Барбершопы')
        ordering = ['name']


class Record(models.Model):
    """Модель записи"""
    name = models.CharField(
        max_length=20,
        verbose_name=_('Имя клиента'),
    )

    barber_name = models.CharField(
        max_length=20,
        verbose_name=_('Имя сотрудника'),
    )

    today = int(datetime.now().day)
    month = int(datetime.now().month)

    if month == 2:
        if today == 28:
            month += 1
            today = 0
    if month in (4, 6, 9, 11):
        if today == 30:
            month += 1
            today = 0
    if month in (1, 3, 5, 7, 8, 10, 12):
        if today == 31:
            month += 1
            today = 0
    if month > 12:
        month = 1

    record_date_CHOICES = [
        (None, 'Выберите дату записи'),
        ('tomorrow_12', f'{str(today + 1)}.{str(month)} в 12:00'),
        ('tomorrow_16', f'{str(today + 1)}.{str(month)} в 16:00'),
        ('tomorrow_20', f'{str(today + 1)}.{str(month)} в 20:00'),
        ('d_a_tomorrow_12', f'{str(today + 2)}.{str(month)} в 12:00'),
        ('d_a_tomorrow_16', f'{str(today + 2)}.{str(month)} в 16:00'),
        ('d_a_tomorrow_20', f'{str(today + 2)}.{str(month)} в 20:00'),
    ]

    record_date = models.CharField(
        max_length=40,
        choices=record_date_CHOICES,
        verbose_name='Дата записи',
    )

    bshop = models.ForeignKey(
        BShop,
        on_delete=models.PROTECT,
        verbose_name='Барбершоп',
    )

    class Meta:
        verbose_name = _('Запись')
        verbose_name_plural = _('Записи')
        ordering = ['record_date']
