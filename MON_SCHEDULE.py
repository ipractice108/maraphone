import monday
import tuesday
import wednsday
import thursday
import friday
import saturday
import sunday
import schedule
import time
import pytz
from datetime import datetime
import calendar
from db import Database
import constants

database = Database(constants.bot_database)

def send_by_schedule():
    print('send_by_schedule')

    now = datetime.now(pytz.timezone('UTC'))
    for assigned_chat in database.get_chats_for_schedule():
        user_time = now.astimezone(pytz.timezone(assigned_chat['timezone']))
        user_time_srt = user_time.strftime('%H:%M')

        calendar_day = calendar.day_name[user_time.weekday()]

        if calendar_day == 'Thursday':
            if   user_time_srt == "06:50": thursday.job_thu1(assigned_chat['id'])
            elif user_time_srt == "07:00": thursday.job_thu2(assigned_chat['id'])
            elif user_time_srt == "07:10": thursday.job_thu3(assigned_chat['id'])
            elif user_time_srt == "07:12": thursday.job_thu33(assigned_chat['id'])
            elif user_time_srt == "07:15": thursday.job_thu4(assigned_chat['id'])
            elif user_time_srt == "10:00": thursday.job_thu5(assigned_chat['id'])
            elif user_time_srt == "12:00": thursday.job_thu6(assigned_chat['id'])
            elif user_time_srt == "15:00": thursday.job_thu7(assigned_chat['id'])
            elif user_time_srt == "20:00": thursday.job_thu8(assigned_chat['id'])
            elif user_time_srt == "21:50": thursday.job_thu9(assigned_chat['id'])

def run_schedule():
    print("running_schedule")
    schedule.every(1).minutes.do(send_by_schedule)
    '''
    monday.mon_schedule()
    tuesday.tue_schedule()
    wednsday.wed_schedule()
    thursday.thu_schedule()
    friday.fri_schedule()
    saturday.sat_schedule()
    sunday.sun_schedule()
    '''

    while True:
        print("schedule_going")
        schedule.run_pending()
        time.sleep(10)
