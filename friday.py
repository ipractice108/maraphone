from bot108 import bot
import schedule

import constants
from db import Database

database = Database(constants.bot_database)
# FRIDAY SCHEDULE
# wake up
def job_fri1():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'Добрейшего утра!) \n,'
                                                  '\n'
                                                  'Время просыпаться, запускать сознание и тело для новых свершений!\n,'
                                                  'Сегодня тебя ждет день "Звука". Вытянись пальцами руки и пальцами ног в разные стороны вытягивая позвоночник.  Определи ногу с которой ты встаешь и вперед на водные процедуры.')

# почистить зубы
def job_fri2():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'Пожалуйста возьмите зубную щетку в непривычную для Вас руку. \n, '
                                                  'Это упражнение благотворно влияет на гармонизацию левого и правого полушария, стабилизируя психику и работу нервной системы \n'
                                                  '\n'
                                                  'По рекомендациям авторитетных стоматологов, для более эффективного результата и мягкого воздействия на десны, чистить зубы необходимо по направлению от основания зуба. Начиная от задних зубов, пройдитесь сначала по верхнему ряду, затем по нижнему. После помассируйте десны и уздечку языка указательными пальцами.')

# waterfasting
def job_fri3():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'Выпейте стакан воды комнатной температуры натощак и за ним второй с цепоткой курскумы и чистым лимонным соком.')

def job_fri33():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'],
                                 'Если захочется есть, попейте еще воды, постарайте позавтракать первый раз вв 13.00')

# warm up + food notice
def job_fri4():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'https://youtu.be/2j3MsZ4E6iQ')
        bot.send_message(assigned_chat['id'], 'В 10.00 вы получите нопоминание о режиме питания + полезные свойства фруктов')

# warm up + food notice
def job_fri5():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'Фрукты.\n'
                                                  'Полезные свойства -  ………')
        bot.send_message(assigned_chat['id'], 'В 12.00 вы получите рецепт обеда')

# lounch recipie
def job_fri6():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'Рецепт на обед - гречка/ овощи рецепт ……..\n'
                                                  '\n'
                                                  'Пожалуйста постарайтесь воздержаться от еды начиная с 18.00. 		конечно если вечером перед сном вы выпьете немного мятного или травяного чаю с минимальным количеством натуральных сладостей ничего критичного не произойдет. \n'
                                                  '\n'
                                                  'Вечером я пришлю Вам следующий комплекс упражнений марафона.')

# evening lesson
def job_fri7():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'Напоминаю, крайний прием пишщи до 18.00')

def job_fri8():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'http://youtu.be/8EgiMc5iwGg', '\n'
                                                                                 '\n'
                                                                                 'выполняйте практику в спокойном темпе, за полчаса перед сном.' '\n'
                                                                                 '\n'
                                                                                 'пожалуйста, постарайтель лечь до 11.00')

# have a good night
def job_fri9():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'Доброй ночи, надеюсь Вам понравилось! Завтра ждет пятый день марафона и новая программа!')

def job_fri10():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'OM NAMAH SHIVAYA')
# -------------------------------------------------------------------------------------------------------------------------

    # FRIDAY SCHEDULE
def fri_schedule():
    schedule.every(1).friday.at("07:00").do(job_fri1)
    schedule.every(1).friday.at("07:15").do(job_fri2)
    schedule.every(1).friday.at("07:30").do(job_fri3)
    schedule.every(1).friday.at("07:32").do(job_fri4)
    schedule.every(1).friday.at("08:30").do(job_fri33)
    schedule.every(1).friday.at("11:00").do(job_fri5)
    schedule.every(1).friday.at("12:00").do(job_fri6)
    schedule.every(1).friday.at("15:00").do(job_fri7)
    schedule.every(1).friday.at("20:00").do(job_fri8)
    schedule.every(1).friday.at("22:50").do(job_fri9)
    schedule.every(1).second.do(job_fri10)