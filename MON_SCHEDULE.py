import monday
import tuesday
import wednsday
import thursday
import friday
import saturday
import sunday
import schedule
import time

def run_schedule():
    print("running_schedule")
    monday.mon_schedule()
    tuesday.tue_schedule()
    wednsday.wed_schedule()
    thursday.thu_schedule()
    friday.fri_schedule()
    saturday.sat_schedule()
    sunday.sun_schedule()


    while True:
        print("schedule_going")
        schedule.run_pending()
        time.sleep(10)
