import os,sys
import constants
import logging

from bot108 import bot
import telebot

#from telebot import types
#from flask import Flask, request

from MON_SCHEDULE import run_schedule

from multiprocessing import Process
logger = telebot.logger
#logging.basicConfig(filename = "bot.log")

#server = Flask(__name__)


#@server.route('/' + constants.token, methods=['POST'])
#def get_message():
#    bot.process_new_updates([types.Update.de_json(
#        request.stream.read().decode("utf-8"))])
#    return "!", 200


#@server.route('/', methods=['GET'])
#def webhook():
#    bot.remove_webhook()
#    bot.set_webhook(url=constants.heroku_url + constants.token)
#    return "Hello from Heroku!", 200


#def run_server():
#    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


if __name__ == "__main__":
    server_process = None
    scheduler_process1 = None

    try:
        #print("starting server")
        #server_process = Process(target=run_server)
        #server_process.start()
        #print(server_process)

        print("starting schedule")
        logger.info('schedule')
        scheduler_process1 = Process(target=run_schedule)
        scheduler_process1.start()
        print(scheduler_process1)


        bot.polling(none_stop=True)

    finally:
        if server_process:
            server_process.terminate()
            server_process.join()

        if scheduler_process1:
            scheduler_process1.terminate()
            scheduler_process1.join()

