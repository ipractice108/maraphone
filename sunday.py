from bot108 import bot
import schedule

import constants
from db import Database

database = Database(constants.bot_database)
# SUNDAY SCHEDULE
# wake up
def job_sun1():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🌝Добрейшего утра! \n'
                                                  '\n'
                                                  '😍Время просыпаться, запускать сознание и тело для новых свершений!\n,'
                                                  '\n'
                                                  '😇Сегодня тебя ждет день "ВОЛЬНОГО ГОЛОДАНИЯ". Вытянись пальцами рук и пальцами ног, вытягивая в разные стороны позвоночник и мышцы тела.  Определи ногу с которой ты встаешь и вперед на водные процедуры.')

# почистить зубы
def job_sun2():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🖖Пожалуйста возьми зубную щетку в непривычную, а может уже и ставшую более послушной и более привыноый для тебя руку. \n, '
                                                  '🧠Продолжаем ежедневно гармонизировать оба полушария головного мозга, укреплять новые нейронные связи и нарабатывать привычку с легкостью выполнять непривычные действия.\n'
                                                  '\n'
                                                  '☝️Чистим зубы от корней зубов к коронкам. После массируем десны и уздечку, да Карл уздечку и десна указательным пальцем правой руки.')

# waterfasting
def job_sun3():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🥛➕🥛➕🍋➕👌➕👌Выпейте стакан воды комнатной температуры натощак и за ним второй с чистым лимонным соком, пищевой содой и щепотокой куркумы. Все как мы уже делали. Для любителей чистки как я, еще добавляю 5-8 капель перекиси водорода.')

def job_sun33():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🥛➕🥛Если захочется есть, попейте еще воды, постарайтесь провести сегодняшний день на воде, максимум на разбавленных свежевыжптых соках')

# warm up + food notice
def job_sun4():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'https://youtu.be/vIpOIkQq704')
        bot.send_message(assigned_chat['id'], '🕙В 10.00 вы получите нопоминание о режиме "голодания" + полезные активности, для отвлечения ума от еды.')

# warm up + food notice
def job_sun5():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '💓О полезных свойствах голодания.\n'
                                                '🤣Я собирался начать с этого марафон, но тогда, вы бы все испугались.'
                                                '🙇Немного поделюсь с вами своими мыслями о настоящей ситуации и затем о пользе голодания'       
                                                '\n'
                                                '🐲Этот МАРАФОН для тех кто хочет управлять своим здоровьем, сознанием и силой воли.\n'
                                                '\n'
                                                '🚀Мы живем в фантастическое время развития технократической цивилизации и постоянной эволюции. На практически неизведанной планете, в абсолютно неизведанном космосе, как фиксирует история, на протяжении тысяч лет, человечество строит идеалы, принципы, придумывает все больше взаимодействий с внешней реальностью и материей, все дальше отдаляясь от своего внутреннего мира, понимания истинного Я и предназначения своего существа.\n'
                                                '\n'
                                                '🏦Капиталистический строй сформировал у людей стремление к большим материальным благам и новым ощущениям, стимулирующим центр удовольствий, посредством легких иллюзорных наслаждений. Сейчас мы не будем разбирать весь спектр влияния внешних факторов на сознание и тело человека ( основой которого является, психология/психосоматика, родовая наследственность и тд.) лишь направим внимание на основные источники жизненной энергии человека.\n'
                                                '\n'
                                                '♻️Дыхание и питание - воздух, вода и пища - основные необходимые элементы для жизнедеятельности организма человека.\n'
                                                '\n'
                                                '🤸‍♀️Чем свободнее протекают все процессы жизнедеятельности, тем легче телу и сознанию, в следствие чего постоянно наблюдается, стабильное хороше настроение и крепкое здоровье. Здоровье и хороше настроение нам нужны для развития и познания устройства вселенского мироздания.\n'
                                                '\n'
                                                '🚖🚎😷При неспокойной жизни, наше тело и внутренние органы трансформировались под предлагаемые условия, так что бы не беспокоить сознание сигналами боли и дискомфорта. Состав воздуха и еды, биоритмы и остальные аспекты жизнедеятельности  человека на данном моменте находятся в дисбалансе.\n'
                                                '\n'
                                                '😤От малоподвижного образа жизни (особенно во время карантина), сидячей работы и вечного влияния гравитационной силы притяжения, компьютера, мобильного телефона и других цифровых агрегатов, позвоночник округляется и деформируется в соответсвии с регулярной задачей смотреть в экран. Вдоль позвоночника находится центральная нервная система которая отвечает за передачу сигнала от мозга ко всем точкам в теле, соотвественно деформация позвоночника ведет к дисбалансу центральной нервной системы и от нее к локальным дисфункциям органов всего организма.\n'
                                                '\n'
                                                '🤦‍♂️Добавим к этим незаметным факторам, ежедневно влияющим на жизнь человека, еще и режим и состав питания. Из за предпочтения выбирать пищу по вкусовым качествам, а не по составу и необходимости, для конкретной конституции тела и жизнедеятельности человека, желудки миллиардов людей страдают от ежедневного несварения и постоянной тяжелой работы, переваривания и проталкивания недостаточно прожеванной еды, сочетание которой невозможно расщепить и усвоить.\n'
                                                '\n'
                                                '😭По сути однодневное голодание — это даже не голодание, а разгрузочный день. Организм наконец-то отдыхает, в первую очередь отдыхает и восстанавливается пищеварительная система, что очень благотворно сказывается на всех процессах, происходящих в организме. Но придётся разочаровать тех, кто думает, что однодневное голодание или голодание в течении 36 часов непременно обернётся потерей веса.\n'
                                                '\n'
                                                '😁чтобы начался настоящий процесс расщепления жировых клеток должно пройти не меньше 3 дней. Организм так устроен, что первые дни жировые запасы сохраняются в целости и сохранности и человек теряет лишь воду. Поэтому напрасно тешить себя мыслью, увидев минус 1 кг на весах, что вы попрощались с 1 кг жировых отложений.\n'
                                                '\n'
                                                '🙊Организм ввиду отсутствия поступления внешних источников питания начинает искать другие резервы, и не только гликоген. Те самые отмершие клетки, которые всё ещё находятся в организме, идут в утилизацию. Этим во многом и объясняется потрясающий эффект сухого голодания, исцеление от недугов во время него и т. д., потому что организм вынужден переработать и избавиться от того, что в нём накопилось за долгое время и что явилось причиной этих недомоганий.\n'
                                                '\n'
                                                '😳Если вы готовы пройти через 36-часовое сухое голодание, то нужно к нему подготовиться. В первую очередь за несколько дней до начала сухого голодания нужно прекратить употреблять в еду животные белки, а непосредственно перед тем, как начать процесс, нужно не забыть очистить кишечник, чтобы во время остановки приёма пищи токсины не попадали в кровь. Это подготовит вас и сделает процесс самого голодания более комфортным.\n'
                                                '\n'
                                                '🤔Ещё лучше, если саму практику голоданий будете проводить после того, как вы всецело в течение длительного времени находились на вегетарианской диете. Хорошо известно, что длительные голодания переносятся веганами и вегетарианцами гораздо легче, не говоря уж о сыроедах.\n'
                                                '\n'
                                                '☝️Не менее важен и процесс выхода из сухого голодания. Время выхода из сухого голодания должно быть равным времени самого голодания. Так как мы в основном говорим о 36-часовом сухом голодании, то и время выхода должно быть равным 24 или 36 часам. Практически это выглядит следующим образом: в течении суток вы не принимаете никакой пищи, на следующий день в течении ещё 12 часов вы продолжаете воздерживаться от еды и питья и только вечером, по прошествии этого времени можно начинать выход.\n'
                                                '\n'
                                                '🥛Выход из сухого голодания лучше начать с приёма небольшого количества воды, а затем через какое-то время можно начинать пить соки. Лучше всего для целей выхода из сухого голодания подходят свежевыжатые соки цитрусовых, хорошо, если они будут немного разбавлены водой, потому что организм за время воздержания от пищи становится весьма восприимчивым к тому, что в него поступает после процесса голодания, поэтому нужно очень тщательно подходить к выбору продуктов и вкусовой интенсивности.\n'
                                                '\n'
                                                '❗️Первые сутки после выхода должны проходить исключительно на соках и лучше всего на свежевыжатых соках цитрусовых: апельсины, мандарины, лимоны, грейпфруты и т. д. Если по каким-то причинам вы не хотите использовать цитрусовые, то отличным вариантом будет гранатовый сок. Он тоже прозрачный и в нём нет клетчатки, тоже самое можно сказать и об ананасовом соке.\n'
                                                '\n'
                                                '✅Все прозрачные соки вам подходят. Исключить придётся те, которые содержат крахмал: морковный, свекольный и т. д. Бананы по той же причине не подходят. Вторые сутки можно уже употреблять в пищу овощи и овощные соки, но лучше в сыром виде. Только после этих двух дней, следующих за 36-часовым воздержанием от пищи, можно возвращаться к обычной термически обработанной пище.\n'
                                                '\n'
                                                '👨‍💻Если ты захочешь узнать еще о голодании, сыроедении и тд. просто гугли читай разные источники и прислушивайся к зравому разуму. Все гармонично и логично складывается, когда знания истины. И пиши мне, поделюсь своим опытом.\n')

# lounch recipie
def job_sun6():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '☕️Сегодня вечером, перед сном выпей немного мятного или травяного чаю без сладостей. \n'
                                                '\n'
                                                '💆‍♂️Сегодня организм отдыхает от постоянного переваривания и проталкивания переработанной/непереработанной пищи, благодря физическим упражнениям, через потовыделения и выделительные системы происходит очищение организма от шлаков, токсинов, и лишних веществ.\n'
                                                '\n'
                                                '🐟🍧🍜🥗🍌🍉🍏Во время марафона, мы постепенно уменьшали количество употребляемой пищи, для поэтапного привыкания тела и сознания к процессам трансформации, новым состояниям и ощущениям. Для тоого что бы безопасно начать процесс эволюции, необходимо сначала полностью очистить организм от ненужных веществ и затем внимательно, также поэтапно запускать процессы осознания вселенского мироздания, аспектов Я и взаимодейсвия с внутренним и окружающими миром.\n'
                                                '\n'
                                                '➡Вечером, я пришлю новое видео с практикой дыхания и медитации, для настройки тела и сознания на благостное, созидательное мышление.')

# evening lesson
def job_sun7():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🌞Напоминаю, сегодня вечером травяной настой или чай без сладостей.')

def job_sun8():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], 'https://youtu.be/vIpOIkQq704' , '\n'
                                                                                 '\n'
                                                                                 '🙆🙆‍♂выполняйте практику в спокойном темпе, за полчаса перед сном.' '\n'
                                                                                 '\n'
                                                                                 '➡пожалуйста, постарайтель лечь до 10.00. Когда мы засыпаем и расслабляемся согласно солнечному и земному биоритму, организм вырабатывает все необходимые гармоны и вещества для усвоения всего полученного опыта.')

# have a good night
def job_sun9():
    for assigned_chat in database.get_chats_for_schedule():
        bot.send_message(assigned_chat['id'], '🙋🏽‍♂Доброй ночи, надеюсь Вам понравилось! Теперь вы готовы к регулярным online занятиям "ipractica.club!" и групповым занятям в классе')
#------------------------------------------------------------------------------------------------------------------------------
# SUNDAY SCHEDULE
def sun_schedule():
        schedule.every(1).sunday.at("08:00").do(job_sun1)
        schedule.every(1).sunday.at("08:30").do(job_sun2)
        schedule.every(1).sunday.at("09:30").do(job_sun3)
        schedule.every(1).sunday.at("10:30").do(job_sun4)
        schedule.every(1).sunday.at("10:00").do(job_sun33)
        schedule.every(1).sunday.at("11:00").do(job_sun5)
        schedule.every(1).sunday.at("12:00").do(job_sun6)
        schedule.every(1).sunday.at("15:00").do(job_sun7)
        schedule.every(1).sunday.at("20:00").do(job_sun8)
        schedule.every(1).sunday.at("22:50").do(job_sun9)






