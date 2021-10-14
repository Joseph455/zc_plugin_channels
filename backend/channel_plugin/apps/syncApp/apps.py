from datetime import datetime,timedelta
from pytz import utc
from .queue_handler import QueueHandler
from .utils import job_run_qhandler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore

from django.apps import AppConfig

scheduler = BackgroundScheduler()
from .queue_handler import QueueHandler as QH, JOIN_TaskHandler, REMOVE_TaskHandler  

class SyncAppConfig(AppConfig):
    name = 'apps.syncApp'

    def ready(self):
        print("The Alpha Dog is here")
        scheduler.add_job(job_run_qhandler, trigger="interval", minutes=10, id="Timer",replace_existing=True,max_instances=1)
        scheduler.start()

    	# # print("App is ready")
    	# QH.run(handlers = [JOIN_TaskHandler, REMOVE_TaskHandler]) 
    	# print("CONCLUDE")
        #  SHould be added to utils .py job function
