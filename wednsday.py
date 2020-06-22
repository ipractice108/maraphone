from bot108 import bot
import schedule

import constants
from db import Database

database = Database(constants.bot_database)
#MONDAY
#wake up
def job_wed1():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🌝Добрейшего утра!) \n,'
                                              '\n'
                                              '🕺Время просыпаться, запускать сознание и тело для новых свершений!\n,'
                                              '🦍Сегодня тебя ждет новый день.  Определи ногу с которой ты встаешь и вперед на утренние процедуры.')
# почистить зубы
def job_wed2():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '👐Пожалуйста возьми зубную щетку в непривычную для тебя руку. \n, '
                                              '⚡️Пусть эта привычка запускает малоактивные части мозга с самого утра и заряжает день уверенностью для решения новых задач. \n'
                                              '\n'
                                              '👉😀Все также чистим зубы от корней к коронкам. Затем массаж десен.')
# waterfasting
def job_wed3():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🥛➕🥛➕🍋➕👌Выпей стакан воды комнатной температуры натощак и за ним второй с 3 чайными ложками лимонного сока и микроскопической щепоткой пищевой соды.')
def job_wed33():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🥛➕🥛Если захочется есть, попей еще воды, постарайся позавтракать первый раз вв 12.30')

# warm up + food notice
def job_wed4():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'https://youtu.be/zVOPQXP587c')
        bot.send_message(assigned_chat['id'], '🕙В 10.00 ты получишь нопоминание о режиме питания + рецепт завтрака')

# warm up + food notice
def job_wed5():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🍧➕🍉Каша с фруктами.\n'
                                                '🌿РАГИ\n'
                                                '💪Также известные как просо пальца и начни, содержат в больших количествах белки, железо и кальций. Индия является ведущим производителем раги в мире. Это цельное зерно считается вегетарианским продуктом и содержит важные аминокислоты, такие как фенилаланин, метионин, изолейцин и лейцин. Раги можно выращивать даже в условиях засухи.\n'
                                                '✅Богатый источник кальция\n'
                                                '✅Волокно способствует ощущению сытости\n'
                                                '✅Много натурального железа\n'
                                                '✅Природный релаксант\n'
                                                '✅Сокращает риск диабета\n'
                                                '✅Улучшает кожу и волосы\n'
                                                '\n'
                                                '❇Есть два вида - зерновая и мука РАГИ. В случае с зернышками, варим их около 30-40 мин на средней интенсивности жара. Если готовим кашу из муки РАГИ, то заливаем кипятком доводя до состояния полужудкой каши. Добавляем фрукты по вкусу. Вкус у каши интеерсный, возможно фруктов захоечтся добавить чуть больше чем обычно.')
        bot.send_message(assigned_chat['id'], '🕙В 12.00 ты получишь рецепт обеда')
# lounch recipie
def job_wed6():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🍘➕🥗Кус кус с овощами.\n'
                                              '\n'
                                              '🌍Еще одно «производное» из пшеничной крупы, изобретенное в Африке. И сегодня в Марокко, Алжире, Ливии и Тунисе кускус — традиционное блюдо. Его подают как с рыбой, так и с овощами, сухофруктами и даже орехами. Готовят из мелкой манной крупы, которую сбрызгивают водой, формируют крупинки, обсыпают их сухой манкой, просеивают и высушивают. Иногда кускус делают из ячменя или риса.\n'
                                              '\n'
                                              '💁достаточно залить кипятком и оставить под крышкой на 5 минут.\n'
                                              '\n'
                                              '👨‍🍳Рецепт - 1 стакан кускуса, 1,5 стакана горячей воды, соль по вкусу. Салат или нарезаные огурцы, листья слата, базилик, немного сельдерея, растительное масло и пару столовых ложек ТАХИНЫ.\n'
                                              '\n'
                                              '🙏Пожалуйста постарайся воздержаться от еды начиная с 19.00. 		конечно если вечером, перед сном ты выпьешь немного мятного или травяного чаю, с минимальным количеством натуральных сладостей ничего критичного не произойдет. \n'
                                              '\n'
                                              '➡Вечером я пришлю  следующее видео с практикой.')
# evening lesson
def job_wed7():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🗓Напоминалочка, крайний прием пишщи до 19.00')

def job_wed8():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'https://youtu.be/R68HosozdtA\n'
                                                                             '\n'
                                                                             '🙆🙆‍♂выполняйте практику в спокойном темпе, за полчаса перед сном.' '\n'
                                                                             '\n'
                                                                             '🙏Пожалуйста, постарайся лечь до 00.00')
# have a good night
def job_wed9():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🙋🏽‍♂Доброй ночи, надеюсь тебе понравилось! Завтра ждет четвертый день марафона и новая программа!')
# -------------------------------------------------------------------------------------------------------------------------

def wed_schedule():
 # WEDNSDAY SCHEDULE
    schedule.every(1).wednesday.at("06:50").do(job_wed1)
    schedule.every(1).wednesday.at("07:00").do(job_wed2)
    schedule.every(1).wednesday.at("07:10").do(job_wed3)
    schedule.every(1).wednesday.at("07:12").do(job_wed33)
    schedule.every(1).wednesday.at("07:15").do(job_wed4)
    schedule.every(1).wednesday.at("10:00").do(job_wed5)
    schedule.every(1).wednesday.at("12:00").do(job_wed6)
    schedule.every(1).wednesday.at("15:00").do(job_wed7)
    schedule.every(1).wednesday.at("20:00").do(job_wed8)
    schedule.every(1).wednesday.at("21:30").do(job_wed9)

