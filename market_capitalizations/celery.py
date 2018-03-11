from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from tasks import save_exchange_rates

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'market_capitalizations.settings')

app = Celery('market_capitalizations')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

#''' from celery.schedules import crontab
#app.conf.beat_schedule = {
#    'add-every-5-seconds': {
#        'task': 'save_exchange_rates_task',
#        'schedule': 600.0,
 #       #'args': (16, 16)
 #   },
#} '''
    