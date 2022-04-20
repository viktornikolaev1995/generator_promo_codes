import uuid
from django.db import models


class Group(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name='Наименование группы')
    amount = models.IntegerField(verbose_name='Число промо-кодов')

    def __str__(self):
        return self.name


class PromoCode(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name='Наименование группы',
        related_name='promo_codes'
    )
    key = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Промо-код')

    def __str__(self):
        return f'{self.group} - {self.key}'
