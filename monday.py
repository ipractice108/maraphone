from bot108 import bot
import schedule

import constants
from db import Database

database = Database(constants.bot_database)
#MONDAY
#wake up
def job_mon1(chat_id):
    bot.send_message(chat_id, '🌝Добрейшего утра!) \n'
                                          '\n'
                                          '🤸‍♂️Время просыпаться, запускать сознание и тело для новых свершений!\n'
                                          '🕺Сегодня тебя ждет новый день.  Определи ногу с которой ты встаешь и вперед на утренние процедуры. ')
#почистить зубы
def job_mon2(chat_id):
    bot.send_message(chat_id, '🖖Пожалуйста возьми зубную щетку в непривычную для тебя руку. \n '
                                            '🧠Это упражнение благотворно влияет на гармонизацию левого и правого полушария, стабилизируя психику и работу нервной системы. \n'
                                          '\n'
                                            '👩‍⚕️По рекомендациям авторитетных стоматологов, для более эффективного результата и мягкого воздействия на десны, чистить зубы необходимо по направлению от корней зубов к коронкам. Начиная от задних зубов, пройдитесь сначала по верхнему ряду, затем по нижнему.\n'
                                            '\n'
                                            '👉😀Настоятельно рекомендую массажировать пальцем десна, питание зубов идет от корней через микроскопические кровеносные каппиляры, соотвественно стимуляция кровотока в деснах благотворно влияет на состояние структуры зубов')
#waterfasting
def job_mon3(chat_id):
    bot.send_message(chat_id, '🥛Пьем стакан воды комнатной температуры натощак.')

#warm up + food notice
def job_mon4(chat_id):
    bot.send_message(chat_id, 'https://youtu.be/cqP85i9NBUY')
    bot.send_message(chat_id, 'Делаем все в комфортной скорости и комфортной амплитуде')
    bot.send_message(chat_id, '➡️В 10.00 ты получишь нопоминание о режиме питания + рецепт завтрака')

# warm up + food notice
def job_mon5(chat_id):
    bot.send_message(chat_id, '🕛с 12.00 - Первый приём пищи, фрукты с кашей на воде.\n'
                                            '\n'
                                            '💪Наиболее здоровый завтрак можно считають каши (кроме рисовой из шлифованного риса и манной) в сочетании с !НЕКИСЛЫМИ! фруктами. При таком сочетании простые углеводы (сахароза, глюкоза, фруктоза и др.), содержащиеся в сладких фруктах, легко усваиваются и стимулируют быстрый выброс инсулина поджелудочной железой. А неперевариваемые пищевые волокна (целлюлоза, гемицеллюлоза, пектин), которые есть во фруктах и кашах, замедляют усвоение сахаров, как следствие и выброс инсулина, снижая нагрузку на поджелудочную железу. Также, это блюдо важно для профилактики сахарного диабета и ожирения.\n'
		                                    '\n'
		                                    '🌱➕🍌Пшеничная каша с фруктами\n'
                                            '🔆Богата витаминами и полезными микроэлементами. Содержит витамины группы В, а также А, Е, F, калий, кальций, магний, цинк, фосфор и молибден. Клетчатка улучшает перистальтику кишечника, способствует мягкому очищению организма от шлаков, токсинов и солей тяжелых металлов.\n'
                                            '\n'
                                            '☝️C пшеной кашей лучше всего сочетаются и усваиваются: \n'
                                            '✅фрукты - яблоки, груши, бананы, арбузы, ананасы, абрикосы, клубника, черника, малина\n'
                                            '✅сухофрукты - курага, чернослив, изюм\n'
                                            '\n')

def job_mon55(chat_id):
    bot.send_message(chat_id, '✅масло\n'
                                            'Сливочное масло: польза и вред\n'
                                            'Польза. Сливочное масло — продукт переработки коровьего молока, содержащий большое количество витамина А, необходимого для построения клеточных мембран, роста, развития, нормального зрения, антиоксидантной и иммунной защиты организма. В этом смысле сливочное масло является уникальным продуктом питания, не сравнимым ни с одним другим жиром. В сливочном масле есть жирорастворимые витамины D, К, Е, РР, которые усваиваются исключительно в жировой среде. Эти вещества необходимы человеку для роста и развития скелета, зубов, кожи и ее придатков, нормальной работы нервной и репродуктивной систем. Сливочное масло — источник мононенасыщенной олеиновой кислоты, более 150 жирных кислот, в том числе 20 незаменимых, которые расходуются на энергетические нужды и используются для построения мембран клеток. Калий, кальций, магний, марганец, железо, хром, медь, фосфор, натрий, цинк — далеко не полный список важных для человека микроэлементов, обнаруженных учеными в молочном продукте. Вред. Сливочное масло калорийно, один его грамм содержит 7,29 ккал. Налегая на этот продукт, можно прибавить в весе и нажить себе кучу проблем, связанных с ожирением. Продукт нуждается в дозированном потреблении, его безопасная суточная норма составляет 10–30 г. Употребление большого количества сливочного масла чревато повышением уровня холестерина в крови и при наличии предрасположенности может привести к атеросклеротическому поражению кровеносных сосудов со всеми вытекающими последствиями.\n'
                                            '\n'
                                            'Растительное масло: польза и вред\n'
                                            'Нельзя однозначно сказать, полезно или вредно растительное масло. Его свойства зависят даже не от сорта и источника происхождения, а от вида отжима и степени очистки. Масла, которые получают методом холодного прессования, считаются наиболее полезными, сохраняющими природные качества масличного растения. Если в названии продукта присутствуют слова Extra Virgin, можно быть уверенным, что в нем присутствуют все витамины и биологически активные органические компоненты. Такое масло имеет особый аромат, вкус, придает блюдам пикантность, но при термической обработке начинает пениться, гореть, приобретает неприятный вкус, токсические и канцерогенные свойства. Растительные масла, полученные методом горячего отжима, содержат меньше полезных веществ, чем те, что получены при холодном отжиме, но настоящим «лидером» по бесполезности считаются экстрагированные масла. При производстве экстрагированных масел жиры извлекают из сырья с помощью растворителей, а затем очищают. Такие масла называют рафинированными, они долго хранятся, не прогоркают, не искажают запаха и вкуса блюд, не горят при термической обработке. Однако при экстрагировании теряются все витамины и полиненасыщенные растительные стеролы, в масле остается «чистый» жир, лишенный полезных качеств, за исключением, пожалуй, энергетической ценности. Да, рафинированное растительное масло не содержит холестерина, как, впрочем, и любой другой растительный продукт, ведь холестерин — вещество животного происхождения. Но дело даже не в этом: очищенное, рафинированное, дезодорированное масло не обладает способностью снижать уровень холестерина в крови, которым обладают масла Extra Virgin, содержащие полиненасыщенные жирные кислоты.\n'
                                            '\n'
                                            '👨‍🍳Рецепт - заливаем пшенку водой, на 2 см выше уровня крупы, доводим до кипения. Варим около 20-30 минут. Затем добавляем фрукты и масло по вкусу.\n'
                                            '\n'
                                            '⚖️Помни! Умеренность - один из важнейших аспектов всех практик. Этот витаминно энергитический заряд здоровой пищи, тоже необходимо употреблять размеренными порциями. Насыщение приходит только спустя некоторое время, при тщательном пережевывании еды, усвоение происходит более качественно. Представь объем своего желудка и приготовь себе подходящую порцию. ')

    bot.send_message(chat_id, '🕛В 12.00 ты получишь рецепт обеда')
#lounch recipie
def job_mon6(chat_id):
    bot.send_message(chat_id, '🍚➕🥗Рис с овощами и рыбой.\n'
                                        '👍Польза риса обусловлена его уникальным составом. Это в основном растительные белки; углеводы (представлены крахмалом); витамины группы В, РР; фолиевая кислота; различные микроэлементы: калий, фосфор, железо, натрий, кремний и т. д.'
                                        '\n'
                                        '🔬Польза и вред продукта с учетом его сорта:\n'
                                        '❇️Дикий рис имеет высокую цену. Связано это с определенными сложностями выращивания, так как требуется доступ к воде. В его составе много протеинов, обеспечивающих мышечную силу и активность. Он ценен микроэлементами, положительно влияет на иммунитет.\n'
                                        '\n'
                                        '❇️Бурый рис является источником селена, магния, марганца, витаминов группы В. Используется в профилактическом питании при онкологии, заболеваниях сердечно-сосудистой системы, при избытке жировой ткани для похудения.\n' 
                                        '\n'
                                        '❇️Черный рис содержит максимум клетчатки и занимает лидирующие позиции по составу антиоксидантов среди различных видов риса. Показан при анемии, хрупкости капилляров.\n'
                                        '\n'
                                        '❇️Красный рис отличается высоким содержанием пищевых волокон, что благотворно влияет на работу кишечника, способствует его очищению от токсинов.\n'
                                        '\n'  
                                        '❇️Белый шлифованный рис меньше всего приносит пользы. В нем удалена верхняя оболочка. Его подвергают такой обработке, которая оставляет минимум питательных веществ. Тем не менее, в продаже его много и часто нет альтернативы. Он легко готовится, что и используется в качестве гарнира ко вторым блюдам.\n'
                                        '\n'                                            
                                        '👨‍🍳Рецепт - засыпаем рис в кипящую воду, вымеряем также 2см над уровнем крупы. Варим около 20 мин до желаемой консистенции. Если вы едите рыбу, желательно выбирать наисвежайшую. В овощах старайтесь добавлять меньше пасленловых ( помидор, баклажан, картофель) и болше зеленых ( вся зелень, огурец, салат, перец, капуста, стручковый горох, броколли и тд.)'    
                                        '\n'
		                                '🙏Пожалуйста постарайся воздержаться от еды после  19.00. 		Конечно если вечером, перед сном ты выпьешь немного мятного или травяного чаю с минимальным количеством натуральных сладостей, ничего критичного не произойдет. \n'
                                        '\n'
                                        '➡️Вечером я пришлю следующее видео с практикой.')

def job_mon66(chat_id):
    bot.send_message(chat_id, 'https://youtu.be/ppzhUe0eZwQ')

#evening lesson
def job_mon7(chat_id):
    bot.send_message(chat_id, 'https://youtu.be/tc8fIUumABM \n'
                         '\n'
                        '🙆🙆‍♂️выполняем практику в спокойном темпе, за полчаса перед сном.' '\n'
                        '\n'
                         '🙏пожалуйста, постарайся лечь до 00.00')

#have a good night
def job_mon8(chat_id):
    bot.send_message(chat_id, '🙋🏽‍♂️️Доброй ночи, надеюсь тебе понравилось! Завтра ждет второй день марафона и новая программа!')


#-------------------------------------------------------------------------------------------------------------------------
# MONDAY SCHEDULE

''' 
def mon_schedule():
    schedule.every(1).monday.at("07:00").do(job_mon1)
    schedule.every(1).monday.at("07:15").do(job_mon2)
    schedule.every(1).monday.at("07:20").do(job_mon3)
    schedule.every(1).monday.at("07:32").do(job_mon4)
    schedule.every(1).monday.at("10:00").do(job_mon5)
    schedule.every(1).monday.at("12:00").do(job_mon6)
    schedule.every(1).monday.at("20:00").do(job_mon7)
    schedule.every(1).monday.at("21:00").do(job_mon8)
'''

