import monday
import thursday
import friday
import schedule
import time


def run_schedule():
    monday.mon_schedule()
    thursday.thu_schedule()
    friday.fri_schedule()

    while True:
        schedule.run_pending()
        time.sleep(10)
