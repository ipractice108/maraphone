from bot108 import bot
import schedule

import constants
from db import Database

database = Database(constants.bot_database)
#MONDAY
#wake up
def job_tue1():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🌝Добрейшего утра!) \n,'
                                          '\n'
                                          '🤸‍♂Время просыпаться, запускать сознание и тело для новых свершений!\n,'
                                          '🕺Сегодня тебя ждет новый день.  Определи ногу с которой ты встаешь и вперед на утренние процедуры. ')
        # почистить зубы

def job_tue2():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🖖Пожалуйста возьми зубную щетку в непривычную для тебя руку. \n, '
                                          '🧠Регулярно практикуя это простое действие, сознание учится привыкать к непривычному, это мировосприятие хорошо помогает в изучении новой информации умений. \n'
                                          '\n'
                                          '👉😀Помним для более эффективного результата и мягкого воздействия на десны, чистить зубы от корней к коронкам. Начиная от задних зубов, сначала по верхнему ряду, затем по нижнему. Массаж десен.')
        # waterfasting

def job_tue3():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🥛Выпейте стакан воды комнатной температуры натощак и за ним сразуже второй.\n'
                                              'ВИДЕО ГДЕ ПЬЮ ДВА СТАКАНА ВОДЫ')

def job_tue33():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🥛➕🥛➕🥛Если захочется есть, попейте еще воды, постарайтесь позавтракать первый раз в 12.30')

        # warm up + food notice

def job_tue4():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'https://youtu.be/EAxW2ivMkpw')
        bot.send_message(assigned_chat['id'], '🕙В 10.00 ты получишь нопоминание о режиме питания + рецепт завтрака')

        # warm up + food notice

def job_tue5():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🍧➕🍌Каша с фруктами.\n'
                                          '🌱Овсянка с фруктами\n'
                                        '💪Полезные свойства овсяной каши для организма связаны с многочисленными витаминами и микроэлементами в ее составе.\n' 
                                        '2️⃣существуют 2 разновидности хлопьев, обладающих собственными специфическими свойствами:\n'
                                        '❇️«Экстра»\n'
                                        '❇️«Геркулес».\n'
                                        '❕Кроме того, сама крупа делится на 2 вида, каждый из которых, в свою очередь, бывает высшего, I и II сорта:\n''
                                        '❇недробленый\n'
                                        '❇плющеный.\n'
                                        '\n'
                                        '⚡️В овсяной каше содержаться:\n'
                                        '✅витамины группы B и E\n'
                                        '✅бета - каротин\n'
                                        '✅марганец\n'
                                        '✅фосфор\n'
                                        '✅натрий\n'
                                        '✅магний\n'
                                        '✅калий\n'
                                        '✅фтор\n'
                                        '☝️Кроме того, в овсе езьм все полезные органические кислоты, среди которых - никотиновая, щавелевая, эруковая и фолиевая. Каша из овса также является богатым источником клетчатки.'
                                        '\n'
                                        '👨‍🍳Рецепт - отмеряем порцию каши размером с кулак и заливаем кипятком, разбавляя на глаз до шидкообразного состояния. Сладкие фрукты, сухофрукты, и масло по вкусу !в очень умеренных количествах!')

        bot.send_message(assigned_chat['id'], '🕛В 12.00 ты получишь рецепт обеда')
        # lounch recipie

def job_tue6():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🍘➕🥗Булгур с овощами.\n'
                                            '\n'
                                            '💪Булгур содержит витамины (Е, К, РР, группы В), минеральные элементы, белки, углеводы, насыщенные и ненасыщенные жирные кислоты (стеариновую, каприловую, пальмитиновую, миристиновую, линолевую, линоленовую, пальмитолеиновую, омега-3, омега-6, омега-9), глютен, клетчатку. По количеству фосфора булгур в 2 раза превосходит манку, а по содержанию кальция – гречку, благодаря чему может стать достойной альтернативой молочным продуктам. Также булгур занимает лидирующее положение среди круп по содержанию калия и магния, не уступает шпинату по концентрации железа, а моркови – по наличию бета-каротина.'   
                                            '\n'
                                            '✅восстанавливает обмен веществ\n'
                                            '✅избавляет от головной боли и головокружений\n'
                                            '✅уменьшает уровень холестерина\n'
                                            '✅повышает концентрацию гемоглобина, благодаря чему лечит анемию\n'
                                            '✅придает прочность зубам, ногтям и костям, предотвращая остеопороз\n'
                                            '✅замедляет старение'
                                            '✅понижает вероятность образования камней в желчном пузыре\n'
                                            '✅служит для профилактики раковых заболеваний\n'
                                            '\n' 
                                            '❗️Из-за присутствия глютена крупу нельзя употреблять при непереносимости этого вещества, обострении панкреатита, возрасте менее трех лет и в первые 3-4 месяца после родов. При повышенной желудочной кислотности, гастрите, язве и рефлюксе можно есть кашу не чаще раза в неделю. Стоит ограничить ее потребление и при холецистите.\n' 
                                            '\n'   
                                            '👨‍🍳Рецепт - насыпаем горсть булгура, заливаем водой на 1,5см выше уровня крупы в кастрюльке и варим. Как обэд начинает закипать снижаем интенсивность жара комфорки. Добавляем специи по вкусу, прекрасно сочестается гималайская соль и различные сочетания масалы, перца. Следим чтобы вода насытила булгур и равномерно выкипела. В результате получаем рассыпчатую вкусноту.\n'
                                            '🥒Салат или овобщи с цельной структурой, все также преимущественно зеленые. Добавляем тахину, оливковое или кунжутное или любое другое раститетельое масло на овощи и чайную ложку соевого соуса в булгур. ПРИЯТНОГО АППЕТИТА!\n'
                                            '\n' 
                                            '🙏Пожалуйста постарайся воздержаться от еды начиная с 19.00. 		конечно если вечером перед сном ты выпьешь немного мятного или травяного чаю с минимальным количеством натуральных сладостей, ничего критичного не произойдет. \n'
                                            '\n'
                                            '➡Вечером я пришлю следующее видео с практикой.')
# evening lesson

def job_tue7():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🗓Напоминаю, крайний прием пишщи до 18.00')

def job_tue77():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '😋Заканчиваем есть!) Мини перекусы тоже считаются!)')



def job_tue8():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'https://youtu.be/FsLWLBmdlXk', '\n'
                                                                         '\n'
                                                                         '🙆🙆‍♂выполняйте практику в спокойном темпе, за полчаса перед сном.' '\n'
                                                                         '\n'
                                                                         '🙏пожалуйста, постарайся лечь до 00.00')

        # have a good night

def job_tue9():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🙋🏽‍♂Доброй ночи, надеюсь Вам понравилось! Завтра ждет третий день марафона и новая программа!')
# -------------------------------------------------------------------------------------------------------------------------
#TUESDAY SCHEDULE

def tue_schedule():
    schedule.every(1).monday.at("06:50").do(job_tue1)
    schedule.every(1).monday.at("07:00").do(job_tue2)
    schedule.every(1).monday.at("07:15").do(job_tue3)
    schedule.every(1).monday.at("07:17").do(job_tue33)
    schedule.every(1).monday.at("07:25").do(job_tue4)
    schedule.every(1).monday.at("10:00").do(job_tue5)
    schedule.every(1).monday.at("12:00").do(job_tue6)
    schedule.every(1).monday.at("16:00").do(job_tue7)
    schedule.every(1).monday.at("17:40").do(job_tue77)
    schedule.every(1).monday.at("19:30").do(job_tue8)
    schedule.every(1).monday.at("21:00").do(job_tue9)

