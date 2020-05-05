import monday
import schedule

'''
monday.job_mon1()
monday.job_mon2()
monday.job_mon3()
monday.job_mon4()
monday.job_mon5()
monday.job_mon6()
monday.job_mon7()
monday.job_mon9()
'''
def mon_schedule():
    schedule.every(1).monday.at("07:00").do(monday.job_mon1)
    schedule.every(1).monday.at("07:15").do(monday.job_mon2)
    schedule.every(1).monday.at("07:30").do(monday.job_mon3)
    schedule.every(1).monday.at("07:32").do(monday.job_mon4)
    schedule.every(1).monday.at("10:00").do(monday.job_mon5)
    schedule.every(1).monday.at("12:00").do(monday.job_mon6)
    schedule.every(1).monday.at("21:00").do(monday.job_mon7)
    schedule.every(1).monday.at("21:00").do(monday.job_mon8)
    schedule.every(1).minute.do(monday.job_mon9)

    while True:
        schedule.run_pending()