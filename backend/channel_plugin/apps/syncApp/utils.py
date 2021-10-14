from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from datetime import datetime,timedelta
from pytz import utc
from .queue_handler import QueueHandler

scheduler = BackgroundScheduler()
def job_run_qhandler():
    print(datetime.now().time().strftime('%H:%M:%S'))
    # QueueHandler.run(dummyHandler)
