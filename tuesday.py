import schedule
#TUESDAY
# wake up
def job_tue1():
        bot.send_message(message.chat.id, 'Добрейшего утра!) \n,'
                                          '\n'
                                          'Время просыпаться, запускать сознание и тело для новых свершений!\n,'
                                          'Сегодн тебя ждет новый день.  Определи ногу с которой ты встаешь и вперед на водные процедуры. ')
        # почистить зубы

def job_tue2():
        bot.send_message(message.chat.id, 'Пожалуйста возьмите зубную щетку в непривычную для Вас руку. \n, '
                                          'Это упражнение благотворно влияет на гармонизацию левого и правого полушария, стабилизируя психику и работу нервной системы \n'
                                          '\n'
                                          'По рекомендациям авторитетных стоматологов, для более эффективного результата и мягкого воздействия на десны, чистить зубы необходимо по направлению от основания зуба. Начиная от задних зубов, пройдитесь сначала по верхнему ряду, затем по нижнему.')
        # waterfasting

def job_tue3():
        bot.send_message(message.chat.id, 'Выпейте стакан воды комнатной температуры натощак и за ним второй.')

def job_tue33():
        bot.send_message(message.chat.id, 'Если захочется есть, попейте еще воды, постарайте позавтракать первый раз вв 12.30')

        # warm up + food notice

def job_tue4():
        bot.send_message(message.chat.id, 'https://youtu.be/2j3MsZ4E6iQ')
        bot.send_message(message.chat.id, 'В 10.00 вы получите нопоминание о режиме питания + рецепт завтрака')

        # warm up + food notice

def job_tue5():
        bot.send_message(message.chat.id, 'Фрукты с кашей на воде.\n'
                                          'рецепт - каша пшеничная ………')
        bot.send_message(message.chat.id, 'В 12.00 вы получите рецепт обеда')
        # lounch recipie

def job_tue6():
        bot.send_message(message.chat.id, 'Рецепт на обед - рис/ овощи рецепт ……..\n'
                                          '\n'
                                          'Пожалуйста постарайтесь воздержаться от еды начиная с 19.00. 		конечно если вечером перед сном вы выпьете немного мятного или травяного чаю с минимальным количеством натуральных сладостей ничего критичного не произойдет. \n'
                                          '\n'
                                          'Вечером я пришлю Вам следующий комплекс упражнений марафона.')
# evening lesson

def job_tue7():
        bot.send_message(message.chat.id, 'Напоминаю, крайний прием пишщи до 18.00')

def job_tue77():
        bot.send_message(message.chat.id, 'Заканчиваем есть!) Мини перекусы тоже считаются!)')



def job_tue8():
        bot.send_message(message.chat.id, 'http://youtu.be/8EgiMc5iwGg', '\n'
                                                                         '\n'
                                                                         'выполняйте практику в спокойном темпе, за полчаса перед сном.' '\n'
                                                                         '\n'
                                                                         'пожалуйста, постарайтель лечь до 00.00')

        # have a good night

def job_tue9():
        bot.send_message(message.chat.id,
                         'Доброй ночи, надеюсь Вам понравилось! Завтра ждет третий день марафона и новая программа!')
def job_tue10():
        bot.send_message(message.chat.id, 'ПУШКА')
# -------------------------------------------------------------------------------------------------------------------------

def job_tue11():
# TUE SCHEDULE
    schedule.every(1).tuesday.at("07:00").do(job_tue1)
    schedule.every(1).tuesday.at("07:15").do(job_tue2)
    schedule.every(1).tuesday.at("07:30").do(job_tue3)
    schedule.every(1).tuesday.at("07:32").do(job_tue4)
    schedule.every(1).tuesday.at("08:30").do(job_tue33)
    schedule.every(1).tuesday.at("11:00").do(job_tue5)
    schedule.every(1).tuesday.at("12:00").do(job_tue6)
    schedule.every(1).tuesday.at("15:00").do(job_tue7)
    schedule.every(1).tuesday.at("18:00").do(job_tue77)
    schedule.every(1).tuesday.at("20:00").do(job_tue8)
    schedule.every(1).tuesday.at("22:50").do(job_tue9)
    schedule.every(1).minute.do(job_tue10)


    schedule.run_pending()

