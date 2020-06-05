import os,sys
import constants
<<<<<<< HEAD

from bot108 import bot
from telebot import types
from flask import Flask, request

from MON_SCHEDULE import run_mon_schedule
from MON_SCHEDULE import run_thu_schedule
from FRI_SCHEDULE import run_fri_schedule

from multiprocessing import Process
server = Flask(__name__)


@server.route('/' + constants.token, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(
        request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=['GET'])
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=constants.heroku_url + constants.token)
    return "Hello from Heroku!", 200


def run_server():
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


if __name__ == "__main__":
    server_process = None
    scheduler_process1 = None
    scheduler_process2 = None
    scheduler_process3 = None
    try:
        print("starting server")
        server_process = Process(target=run_server)
        server_process.start()
        print(server_process)

        print("starting schedule")
        scheduler_process1 = Process(target=run_mon_schedule)
        scheduler_process1.start()
        print(scheduler_process1)

        print("starting thursday")
        scheduler_process2 = Process(target=run_thu_schedule)
        scheduler_process2.start()
        print(scheduler_process2)

        print("starting friday")
        scheduler_process3 = Process(target=run_fri_schedule)
        scheduler_process3.start()
        print(scheduler_process3)

        bot.polling(none_stop=True)

    finally:
        if server_process:
            server_process.terminate()
            server_process.join()

        if scheduler_process1:
            scheduler_process1.terminate()
            scheduler_process1.join()

        if scheduler_process2:
            scheduler_process2.terminate()
            scheduler_process2.join()

        if scheduler_process3:
            scheduler_process3.terminate()
            scheduler_process3.join()
=======
import telebot
from db import Database

bot = telebot.TeleBot(constants.token)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

database = Database(constants.bot_database)


print(bot.get_me())

def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {} {}, (id = {}) \n Текст - {}".format(message.from_user.first_name,
                                                               message.from_user.last_name,
                                                               str(message.from_user.id),
                                                               message.text))
    print(answer)



@bot.message_handler(content_types=['text', 'video', 'url'])
def handle_text(message):
    print("message text is: " + message.text)

    database.add_chat(message.chat)

    if message.text == "/start":
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Да сегодня понедельник и я готов!')
        send = bot.send_message(message.chat.id, 'Здравствуйте! Начинаем марофон ipractice.club', reply_markup=key)

    elif message.text == "Да сегодня понедельник и я готов!":
        key_remove = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '🏆Этот МАРАФОН для тех кто хочет управлять своим здоровьем, сознанием и силой воли.\n'
                                          '\n'
                                          '📡🚀Мы живем в фантастическое время развития технократической цивилизации и постоянной эволюции. На практически неизведанной планете, в абсолютно неизведанном космосе, как фиксирует история, на протяжении тысяч лет, человечество строит идеалы, принципы, придумывает все больше взаимодействий с внешней реальностью и материей, все дальше отдаляясь от своего внутреннего мира, понимания истинного Я и предназначения своего существа.\n'
                                          '\n'
                                          '💰Капиталистический строй сформировал у людей стремление к большим материальным благам и новым ощущениям, стимулирующим центр удовольствий, посредством легких иллюзорных наслаждений.\n'
                                          '\n'
                                          '🌊Сейчас мы не будем разбирать весь спектр влияния внешних факторов на сознание и тело человека ( основой которого является, психология/психосоматика, родовая наследственность и тд.) лишь направим внимание на основные источники жизненной энергии человека.\n'
                                          '\n'
                                          '👃🥗Дыхание и питание - воздух, вода и пища ( и конечно же ДВИЖЕНИЕ) - основные необходимые элементы для жизнедеятельности организма человека.\n'
                                          '\n'
                                          '🏄Чем свободнее протекают все процессы жизнедеятельности, тем легче телу и сознанию, в следствие чего постоянно наблюдается, стабильное хороше настроение и крепкое здоровье. Здоровье и хороше настроение нам нужны для развития и познания устройства вселенского мироздания.\n'
                                          '\n'
                                          '🏪При неспокойной жизни, наше тело и внутренние органы трансформировались под предлагаемые условия, так что бы не беспокоить сознание сигналами боли и дискомфорта. Состав воздуха и еды, биоритмы и остальные аспекты жизнедеятельности  человека на данном моменте находятся в дисбалансе.\n'
                                          '\n'
                                          '👨‍💻👩‍💻От малоподвижного образа жизни, сидячей работы и вечного влияния гравитационной силы притяжения, компьютера, мобильного телефона и других цифровых агрегатов, позвоночник округляется и деформируется в соответсвии с регулярной задачей смотреть в экран. Вдоль позвоночника находится центральная нервная система которая отвечает за передачу сигнала от мозга ко всем точкам в теле, соотвественно деформация позвоночника ведет к дисбалансу центральной нервной системы и от нее к локальным дисфункциям органов всего организма.   Добавим к этим незаметным факторам, ежедневно влияющим на жизнь человека, еще и режим и состав питания. Из за предпочтения выбирать пищу по вкусовым качествам, а не по составу и необходимости, для конкретной конституции тела и жизнедеятельности человека, желудки миллиардов людей страдают от ежедневного несварения и постоянной тяжелой работы, переваривания и проталкивания плохо прожеванной еды, сочетание которой не возможно расщепить и усвоить.\n'
                                          '\n'
                                          '🙌Мы начинаем МАРАФОН с осознания процессов жизнедеятельности организма и на протяжении марафона, занимаемся подготовкой тела и сознания для новой, здоровой, интересной, счастливой жизни! ', reply_markup=key_remove)
 #кнопка "начнем с дыхания"
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Начнем с дыхания!')
        bot.send_message(message.chat.id, '❗Пожалуйста, прочитайте и посмотрите подготовительную информацию перед началом марафона❗️', reply_markup=key)

    elif message.text == "Начнем с дыхания!":
        key_remove = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '👃Дыхание – одна из важнейших функций регулирования жизнедеятельности человеческого организма, отвечающая за процессусвоения кислорода и выделения углекисолого газа.\n'
                                          '\n'
                                          '❤️В организме человека функцию дыхания обеспечивает дыхательная (респираторная система). Дыхание в организме человека и животных представляет собой процесс использования кислорода клетками тканей в биологическом окислении с образованием энергии и конечного продукта дыхания — углекислого газа.'
                                          '\n'
                                          '✅Дыхательную систему составляют:\n'
                                          '- нос\n'
                                          '- глотка\n'
                                          '- трахея\n'
                                          '- бронхи и легкие\n'
                                          '\n'
                                          '✅В дыхательную систему входят легкие и респираторный тракт (дыхательные пути), который, в свою очередь, включает носовые ходы, гортань, трахею, бронхи, мелкие бронхи и альвеолы \n' 
                                          '\n'
                                          'https://www.youtube.com/watch?v=8OgMs84H670', reply_markup=key_remove)
#кнопка "теперь о ЖКТ и пищеварении"
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Теперь о ЖКТ и пищеварении')
        bot.send_message(message.chat.id, '❗️Пожалуйста, прочитайте и посмотрите подготовительную информацию перед началом марафона❗️', reply_markup=key)

    elif message.text == "Теперь о ЖКТ и пищеварении":
        key_remove = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '🍏Желудочно - кишечный тракт(ЖКТ) или пищеварительный тракт - система органов, перерабатывающих пищу, извлекающих из нее питательные вещества, всасывающих питательные вещества в кровь, выводящих из организма непереваренные остатки.\n'
                                            '\n'
                                          '🎓Органы желудочно - кишечного тракта, а также и вспомогательные органы(слюнные железы, печень, поджелудочная железа, желчный пузырь и др.) составляют систему пищеварения.\n'
                                            '\n' 
                                          '✅К органам(отделам) ЖКТ относятся:\n'
                                            '- рот(ротовая полость, лат. oral cavity)\n'
                                            '- глотка (лат. pharynx)\n'
                                            '- пищевод (лат. œsóphagus)\n'
                                            '- желудок(лат. ventriculus)\n'
                                            '- тонкая кишка(лат. intestinum tenue)\n'
                                            '- толстая кишка(лат. intestinum crassum)\n'
                                          '\n'
                                            '🥗Тонкая кишка состоит из трех отделов:\n'
                                          '1. двенадцатиперстной (лат. duodénum)\n'
                                          '2. тощей (лат. jejunum)\n'
                                          '3. подвздошной (лат. ileum) кишок.\n'
                                          '\n'
                                            '🍌В толстой кишке выделяют три отдела:\n'
                                          '1. слепую кишку (лат. caecum) с червеобразным отростком'
                                          '2. ободочную кишку (лат. colon) \n'
                                          '        с четырьмя подотделами\n'
                                          '                   - восходящая ободочная\n'
                                          '                   - поперечная обоечная\n'
                                          '                   - нисходящая ободочная\n'
                                          '                   - сигмовидная кишки\n'
                                          '3. прямую кишку (лат. rectum) с широкой частью — ампулой прямой кишки и оконечной сужающейся частью — заднепроходным каналом, заканчивающейся анальным отверстием.\n'
                                          '\n'
                                            '✅Тонкая и толстая кишки составляют кишечник.\n'
                                          '\n'
                                          'https://www.youtube.com/watch?v=H2tXzybK2Rg', reply_markup=key_remove)

#немного о ТРАВМБЕЗОПАСНОСТИ и начинаем
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('немного о ТРАВМБЕЗОПАСНОСТИ и начинаем')
        bot.send_message(message.chat.id, '❗️Пожалуйста, прочитайте и посмотрите подготовительную информацию перед началом марафона❗️', reply_markup=key)

    elif message.text == "немного о ТРАВМБЕЗОПАСНОСТИ и начинаем":
        key_remove = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '⛑Травмбезопасность в практике - это ответственность перед самим собой за свои действия.\n'
                                            '\n'
                                            '👁Максимально внимательное отношение к каждому движению в упражнениях и комментариям ( вдоху, выдоху и задержке между ними) дает практикующему гарантию благотворного развития/прогресса, получения новых приятных ощущений в теле и сознании.\n'
                                            '\n'
                                            '🏆В данном марафоне для Вас подготовлена поэтапная, адаптивная последовательность ежедневных комплексов на неделю.   ☝️Все что Вы делаете по видео урокам, необходимо выполнять в пол силы, насколько получается, больше прислушиваясь к своему телу.\n'
                                            '\n'
                                            '❗️Если у Вас есть явные противопоказания к групповым занятиям ( грыжи, протруззи, переломы, растяжения, после родовое восстановление, искривления позвоночника, проблемы с лишним весом, осложнения с давлением и тд.) лучше посоветоваться с авторитетным доктором или пройти индивидуальную консультацию у @shantykungfu\n'
                                            '\n'
                                            'https://www.youtube.com/watch?v=3ZNLp_bWaNk', reply_markup=key_remove)

        bot.send_message(message.chat.id, '❗️Превосходно! Вы получили общие сведения для более осознонаного понимания предстоящего процесса. '
                                          '\n️'
                                          'Теперь, Вы каждый день получаете от меня сообщения с напоминанями о режиме питания, тренировок и отдха')

        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('ВПЕРЕД!')
        bot.send_message(message.chat.id,'❗️Пожалуйста, помните следовать советам и заниматься по видео урокам необходимо в соответсвии со своими ощущениями, без чрезмерных усилий, желательно в пол силы.❗️', reply_markup=key)

    elif message.text == 'ВПЕРЕД!':
      database.update_assign_shedule(message.chat.id)
>>>>>>> 06dec60060077b96e7fb2f6b5dff71d749202e7a
