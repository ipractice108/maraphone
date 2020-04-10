# THURSDAY SCHEDULE
# wake up
 thursday_schedule = "def job_thu1():
        bot.send_message(message.chat.id, 'Добрейшего утра!) \n,'
                                              '\n'
                                              'Время просыпаться, запускать сознание и тело для новых свершений!\n,'
                                              'Сегодня тебя ждет день Осознаного дыхания. Вытянись пальцами руки и пальцами ног в разные стороны вытягивая позвоночник.  Определи ногу с которой ты встаешь и вперед на водные процедуры.')
# почистить зубы
    def job_thu2():
        bot.send_message(message.chat.id, 'Пожалуйста возьмите зубную щетку в непривычную для Вас руку. \n, '
                                              'Это упражнение благотворно влияет на гармонизацию левого и правого полушария, стабилизируя психику и работу нервной системы \n'
                                              '\n'
                                              'По рекомендациям авторитетных стоматологов, для более эффективного результата и мягкого воздействия на десны, чистить зубы необходимо по направлению от основания зуба. Начиная от задних зубов, пройдитесь сначала по верхнему ряду, затем по нижнему.')

# waterfasting
    def job_thu3():
        bot.send_message(message.chat.id, 'Выпейте стакан воды комнатной температуры натощак и за ним второй с цепоткой курскумы и чистым лимонным соком.')

    def job_thu33():
        bot.send_message(message.chat.id, 'Если захочется есть, попейте еще воды, постарайте позавтракать первый раз вв 13.00')

# warm up + food notice
    def job_thu4():
        bot.send_message(message.chat.id, 'https://youtu.be/2j3MsZ4E6iQ')
        bot.send_message(message.chat.id, 'В 10.00 вы получите нопоминание о режиме питания + полезные свойства фруктов')

# warm up + food notice
    def job_thu5():
        bot.send_message(message.chat.id, 'Фрукты.\n'
                                              'Полезные свойства -  ………')
        bot.send_message(message.chat.id, 'В 12.00 вы получите рецепт обеда')

# lounch recipie
    def job_thu6():
        bot.send_message(message.chat.id, 'Рецепт на обед - гречка/ овощи рецепт ……..\n'
                                              '\n'
                                              'Пожалуйста постарайтесь воздержаться от еды начиная с 18.00. 		конечно если вечером перед сном вы выпьете немного мятного или травяного чаю с минимальным количеством натуральных сладостей ничего критичного не произойдет. \n'
                                              '\n'
                                              'Вечером я пришлю Вам следующий комплекс упражнений марафона.')

# evening lesson
    def job_thu7():
        bot.send_message(message.chat.id, 'Напоминаю, крайний прием пишщи до 18.00')

    def job_thu8():
        bot.send_message(message.chat.id, 'http://youtu.be/8EgiMc5iwGg', '\n'
                                                                             '\n'
                                                                             'выполняйте практику в спокойном темпе, за полчаса перед сном.' '\n'
                                                                             '\n'
                                                                             'пожалуйста, постарайтель лечь до 11.30')

# have a good night
    def job_thu9():
        bot.send_message(message.chat.id, 'Доброй ночи, надеюсь Вам понравилось! Завтра ждет пятый день марафона и новая программа!')
# -------------------------------------------------------------------------------------------------------------------------

# THURSDAY SCHEDULE
schedule.every(1).thursday.at("07:00").do(job_thu1)
schedule.every(1).thursday.at("07:15").do(job_thu2)
schedule.every(1).thursday.at("07:30").do(job_thu3)
schedule.every(1).thursday.at("07:32").do(job_thu4)
schedule.every(1).thursday.at("08:30").do(job_thu33)
schedule.every(1).thursday.at("11:00").do(job_thu5)
schedule.every(1).thursday.at("12:00").do(job_thu6)
schedule.every(1).thursday.at("15:00").do(job_thu7)
schedule.every(1).thursday.at("20:00").do(job_thu8)
schedule.every(1).thursday.at("22:50").do(job_thu9)"