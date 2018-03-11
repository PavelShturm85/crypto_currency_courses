from __future__ import absolute_import, unicode_literals
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'market_capitalizations.settings'
import django
django.setup()
import requests
from exchange_rates.models import Currency
import random
import time
from celery.decorators import task
from datetime import datetime


@task(name="save_exchange_rates_task")
def save_exchange_rates(coin):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}/'.format(coin)
    repositories = requests.get(url, timeout=(5.0, 30.0)).json()
    for exchange in repositories:
        last_updated_date = datetime.utcfromtimestamp(int(exchange['last_updated']))
        Currency.objects.create(name=exchange['name'],
                                price_usd=exchange['price_usd'],
                                last_updated=last_updated_date,)


if __name__ == '__main__':
    #save_exchange_rates(coin)
    pass