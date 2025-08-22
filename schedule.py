from apscheduler.schedulers.blocking import BlockingScheduler
from main import main
import logging

logging.basicConfig(level=logging.INFO)

scheduler = BlockingScheduler()

scheduler.add_job(main, 'cron', hour=21, minute=20)

try:
    logging.info("Scheduler started")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    logging.info("Scheduler stopped")