import time
from datetime import datetime
from decimal import Decimal
from django.db import models


# Create your models here.


class Currency(models.Model):
    name = models.CharField('Название валюты', max_length=255)
    price_usd = models.DecimalField(
        'Курс в долларах', max_digits=20, decimal_places=10, blank=True, null=True)
    last_updated = models.DateTimeField('Последние обновление')


    def __str__(self):
        return '%s %s %s' % (self.name, self.price_usd, self.last_updated)
