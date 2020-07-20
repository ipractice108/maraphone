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
        if calendar_day == 'Monday':
            if   user_time_srt == "06:50": monday.job_mon1(assigned_chat['id'])
            elif user_time_srt == "07:00": monday.job_mon2(assigned_chat['id'])
            elif user_time_srt == "07:10": monday.job_mon3(assigned_chat['id'])
            elif user_time_srt == "07:17": monday.job_mon4(assigned_chat['id'])
            elif user_time_srt == "10:00": monday.job_mon5(assigned_chat['id'])
            elif user_time_srt == "12:00": monday.job_mon6(assigned_chat['id'])
            elif user_time_srt == "18:00": monday.job_mon7(assigned_chat['id'])
            elif user_time_srt == "19:30": monday.job_mon8(assigned_chat['id'])


        if calendar_day == 'Tuesday':
            if   user_time_srt == "06:50": tuesday.job_tue1(assigned_chat['id'])
            elif user_time_srt == "07:00": tuesday.job_tue2(assigned_chat['id'])
            elif user_time_srt == "07:10": tuesday.job_tue3(assigned_chat['id'])
            elif user_time_srt == "07:12": tuesday.job_tue33(assigned_chat['id'])
            elif user_time_srt == "07:15": tuesday.job_tue4(assigned_chat['id'])
            elif user_time_srt == "10:00": tuesday.job_tue5(assigned_chat['id'])
            elif user_time_srt == "12:00": tuesday.job_tue6(assigned_chat['id'])
            elif user_time_srt == "15:00": tuesday.job_tue7(assigned_chat['id'])
            elif user_time_srt == "17:40": tuesday.job_tue77(assigned_chat['id'])
            elif user_time_srt == "20:00": tuesday.job_tue8(assigned_chat['id'])
            elif user_time_srt == "21:50": tuesday.job_tue9(assigned_chat['id'])

        if calendar_day == 'Wednsday':
            if   user_time_srt == "06:50": wednsday.job_wed1(assigned_chat['id'])
            elif user_time_srt == "07:00": wednsday.job_wed2(assigned_chat['id'])
            elif user_time_srt == "07:10": wednsday.job_wed3(assigned_chat['id'])
            elif user_time_srt == "07:12": wednsday.job_wed33(assigned_chat['id'])
            elif user_time_srt == "07:15": wednsday.job_wed4(assigned_chat['id'])
            elif user_time_srt == "10:00": wednsday.job_wed5(assigned_chat['id'])
            elif user_time_srt == "12:00": wednsday.job_wed6(assigned_chat['id'])
            elif user_time_srt == "15:00": wednsday.job_wed7(assigned_chat['id'])
            elif user_time_srt == "20:00": wednsday.job_wed8(assigned_chat['id'])
            elif user_time_srt == "21:50": wednsday.job_wed9(assigned_chat['id'])

        if calendar_day == 'Monday':
            if   user_time_srt == "06:50": monday.job_mon1(assigned_chat['id'])
            elif user_time_srt == "07:00": monday.job_mon2(assigned_chat['id'])
            elif user_time_srt == "07:10": monday.job_mon3(assigned_chat['id'])
            elif user_time_srt == "07:17": monday.job_mon4(assigned_chat['id'])
            elif user_time_srt == "10:00": monday.job_mon5(assigned_chat['id'])
            elif user_time_srt == "12:00": monday.job_mon6(assigned_chat['id'])
            elif user_time_srt == "18:00": monday.job_mon7(assigned_chat['id'])
            elif user_time_srt == "19:30": monday.job_mon8(assigned_chat['id'])


        if calendar_day == 'Tuesday':
            if   user_time_srt == "06:50": tuesday.job_tue1(assigned_chat['id'])
            elif user_time_srt == "07:00": tuesday.job_tue2(assigned_chat['id'])
            elif user_time_srt == "07:10": tuesday.job_tue3(assigned_chat['id'])
            elif user_time_srt == "07:12": tuesday.job_tue33(assigned_chat['id'])
            elif user_time_srt == "07:15": tuesday.job_tue4(assigned_chat['id'])
            elif user_time_srt == "10:00": tuesday.job_tue5(assigned_chat['id'])
            elif user_time_srt == "12:00": tuesday.job_tue6(assigned_chat['id'])
            elif user_time_srt == "15:00": tuesday.job_tue7(assigned_chat['id'])
            elif user_time_srt == "17:40": tuesday.job_tue77(assigned_chat['id'])
            elif user_time_srt == "20:00": tuesday.job_tue8(assigned_chat['id'])
            elif user_time_srt == "21:50": tuesday.job_tue9(assigned_chat['id'])

        if calendar_day == 'Wednsday':
            if   user_time_srt == "06:50": wednsday.job_wed1(assigned_chat['id'])
            elif user_time_srt == "07:00": wednsday.job_wed2(assigned_chat['id'])
            elif user_time_srt == "07:10": wednsday.job_wed3(assigned_chat['id'])
            elif user_time_srt == "07:12": wednsday.job_wed33(assigned_chat['id'])
            elif user_time_srt == "07:15": wednsday.job_wed4(assigned_chat['id'])
            elif user_time_srt == "10:00": wednsday.job_wed5(assigned_chat['id'])
            elif user_time_srt == "12:00": wednsday.job_wed6(assigned_chat['id'])
            elif user_time_srt == "15:00": wednsday.job_wed7(assigned_chat['id'])
            elif user_time_srt == "20:00": wednsday.job_wed8(assigned_chat['id'])
            elif user_time_srt == "21:50": wednsday.job_wed9(assigned_chat['id'])

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

        if calendar_day == 'Friday':
            if user_time_srt == "06:50": friday.job_fri1(assigned_chat['id'])
            elif user_time_srt == "07:00": friday.job_fri2(assigned_chat['id'])
            elif user_time_srt == "07:10": friday.job_fri3(assigned_chat['id'])
            elif user_time_srt == "07:12": friday.job_fri33(assigned_chat['id'])
            elif user_time_srt == "07:15": friday.job_fri4(assigned_chat['id'])
            elif user_time_srt == "10:00": friday.job_fri5(assigned_chat['id'])
            elif user_time_srt == "12:00": friday.job_fri6(assigned_chat['id'])
            elif user_time_srt == "15:00": friday.job_fri7(assigned_chat['id'])
            elif user_time_srt == "20:00": friday.job_fri8(assigned_chat['id'])
            elif user_time_srt == "21:50": friday.job_fri9(assigned_chat['id'])

        if calendar_day == 'Saturday':
            if user_time_srt == "06:50": saturday.job_sat1(assigned_chat['id'])
            elif user_time_srt == "07:00": saturday.job_sat2(assigned_chat['id'])
            elif user_time_srt == "07:10": saturday.job_sat3(assigned_chat['id'])
            elif user_time_srt == "07:12": saturday.job_sat33(assigned_chat['id'])
            elif user_time_srt == "07:15": saturday.job_sat4(assigned_chat['id'])
            elif user_time_srt == "10:00": saturday.job_sat5(assigned_chat['id'])
            elif user_time_srt == "12:00": saturday.job_sat6(assigned_chat['id'])
            elif user_time_srt == "15:00": saturday.job_sat7(assigned_chat['id'])
            elif user_time_srt == "20:00": saturday.job_sat8(assigned_chat['id'])
            elif user_time_srt == "21:50": saturday.job_sat9(assigned_chat['id'])

        if calendar_day == 'Sunday':
            if user_time_srt == "06:50": sunday.job_sun1(assigned_chat['id'])
            elif user_time_srt == "07:00": sunday.job_sun2(assigned_chat['id'])
            elif user_time_srt == "07:10": sunday.job_sun3(assigned_chat['id'])
            elif user_time_srt == "07:12": sunday.job_sun33(assigned_chat['id'])
            elif user_time_srt == "07:15": sunday.job_sun4(assigned_chat['id'])
            elif user_time_srt == "10:00": sunday.job_sun5(assigned_chat['id'])
            elif user_time_srt == "12:00": sunday.job_sun6(assigned_chat['id'])
            elif user_time_srt == "15:00": sunday.job_sun7(assigned_chat['id'])
            elif user_time_srt == "20:00": sunday.job_sun8(assigned_chat['id'])
            elif user_time_srt == "21:50": sunday.job_sun9(assigned_chat['id'])


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
