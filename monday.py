from bot108 import bot
import schedule

import constants
from db import Database

database = Database(constants.bot_database)
#MONDAY
#wake up
def job_mon1():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'Добрейшего утра!) \n,'
                                          '\n'
                                          'Время просыпаться, запускать сознание и тело для новых свершений!\n,'
                                          'Сегодн тебя ждет новый день.  Определи ногу с которой ты встаешь и вперед на водные процедуры. ')
#почистить зубы
def job_mon2():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'Пожалуйста возьмите зубную щетку в непривычную для вас руку. \n, '
                                            'Это упражнение благотворно влияет на гармонизацию левого и правого полушария, стабилизируя психику и работу нервной системы \n'
                                          '\n'
                                            'По рекомендациям авторитетных стоматологов, для более эффективного результата и мягкого воздействия на десны, чистить зубы необходимо по направлению от основания зуба. Начиная от задних зубов, пройдитесь сначала по верхнему ряду, затем по нижнему.')
#waterfasting
def job_mon3():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'Выпейте стакан воды комнатной температуры натощак.')

#warm up + food notice
def job_mon4():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'https://youtu.be/2j3MsZ4E6iQ')
      bot.send_message(assigned_chat['id'], 'В 10.00 вы получите нопоминание о режиме питания + рецепт завтрака')

# warm up + food notice
def job_mon5():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'с 12.00 - Первый приём пищи, фрукты с кашей на воде.\n'
		                                    'рецепт - каша пшеничная ………')
      bot.send_message(assigned_chat['id'], 'В 12.00 вы получите рецепт обеда')
#lounch recipie
def job_mon6():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'Рецепт на обед - рис/ овощи рецепт ……..\n'
                                          '\n'
		                                    'Пожалуйста постарайтесь воздержаться от еды начиная с 19.00. 		конечно если вечером перед сном вы выпьете немного мятного или травяного чаю с минимальным количеством натуральных сладостей ничего критичного не произойдет. \n'
                                          '\n'
                                          'Вечером я пришлю Вам следующий комплекс упражнений марафона.')
#evening lesson
def job_mon7():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'http://youtu.be/8EgiMc5iwGg', '\n'
                         '\n'
                        'выполняйте практику в спокойном темпе, за полчаса перед сном.' '\n'
                        '\n'
                         'пожалуйста, постарайтель лечь до 00.00')
#have a good night
def job_mon8():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'Доброй ночи, надеюсь Вам понравилось! Завтра ждет второй день марафона новая программа!')

def job_mon9():
    for assigned_chat in database.get_chats_for_schedule():
      bot.send_message(assigned_chat['id'], 'Кирюха мозг')

#-------------------------------------------------------------------------------------------------------------------------
# MONDAY SCHEDULE


def mon_schedule():
    schedule.every(1).monday.at("07:00").do(job_mon1)
    schedule.every(1).monday.at("07:15").do(job_mon2)
    schedule.every(1).monday.at("07:30").do(job_mon3)
    schedule.every(1).monday.at("07:32").do(job_mon4)
    schedule.every(1).monday.at("10:00").do(job_mon5)
    schedule.every(1).monday.at("12:00").do(job_mon6)
    schedule.every(1).monday.at("21:00").do(job_mon7)
    schedule.every(1).monday.at("21:00").do(job_mon8)
