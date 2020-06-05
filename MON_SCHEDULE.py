import monday
import thursday
import schedule
import time


def run_mon_schedule():
    monday.mon_schedule()

def run_thu_schedule():
    thursday.thu_schedule()


    while True:
        schedule.run_pending()
        time.sleep(10)
