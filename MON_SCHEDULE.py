import monday
import thursday
import friday
import schedule
import time

def run_schedule():
    print("running_schedule")
    monday.mon_schedule()
    thursday.thu_schedule()
    friday.fri_schedule()

    while True:
        print("schedule_going")
        schedule.run_pending()
        time.sleep(10)
