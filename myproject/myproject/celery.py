import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'scrape-proxy-data-every-day': {
        'task': 'scrapper_app.tasks.task_to_scrape_data',
        'schedule': crontab(minute='*/1'),  # Run daily at midnight
    },
}
