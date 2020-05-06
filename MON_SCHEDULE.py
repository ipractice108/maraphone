import monday
import schedule
import time


def run_schedule():
    monday.mon_schedule()

    while True:
        schedule.run_pending()
        time.sleep(10)