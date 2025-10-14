import telebot
import datetime
import time
import threading

bot = telebot.TeleBot("7850891071:AAEPeaUvnKyRpFlLMxf4MSIPKl3gCuys5JI")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello, I'm chat bot that will help you to understand what you eat and how it affects you")
    reminder_thread = threading.Thread(target=send_reminder, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['Poel'])
def eat_message(message):
    bot.reply_to(message,"Have you eat something? Please tell me what")


@bot.message_handler(commands=['Reaction'])
def reaction_message(message):
    bot.reply_to(message, "How do you feel yourself?")

@bot.message_handler(commands=['Help'])
def Help_message(message):
    bot.reply_to(message, "/?How can I help you?")

def send_reminder(chat_id):
    breakfast_time = "08:00"
    lunch_time = "12:00"
    dinner_time = "20:25"
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == breakfast_time or now == lunch_time or now == dinner_time:
            bot.send_message(chat_id, 'Hey! Share what have you eat?')
            time.sleep(61)
        time.sleep(1)



bot.polling(none_stop=True)