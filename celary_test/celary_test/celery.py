import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celary_test.settings')

app = Celery('celary_test')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# test -----------------------------

@app.task(bind=True)
def debug_task(self):
    print('hello celery')

@app.task
def print_hello():
    print('hello celery')

# test ----------------------------

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')