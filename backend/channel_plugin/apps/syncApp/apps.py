from datetime import datetime,timedelta
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore


scheduler = BackgroundScheduler()
def job_function():
    print(datetime.now().time().strftime('%H:%M:%S'))


from django.apps import AppConfig


class SyncAppConfig(AppConfig):
    name = 'apps.syncApp'

    def ready(self):
        print("The Alpha Dog is here")
        scheduler.add_job(job_function, "interval", seconds=5)
        scheduler.start()

