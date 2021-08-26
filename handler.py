import os
import telegram
#  from telegram.ext import Updater, CommandHandler

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def send_poll(event, context):
    bot = telegram.Bot(token=TOKEN)
    questions = ["Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Kann gar nicht"]
    bot.send_poll(
        CHAT_ID,
        "Fusi diese Woche",
        questions,
        is_anonymous=False,
        allows_multiple_answers=True,
    )

#  def start(update, context):
    #  print(update.effective_chat.id)
    #  context.bot.sendMessage(chat_id=update.effective_chat.id, text="Hi!")

#  if __name__ == "__main__":
    #  updater = Updater(token=TOKEN, use_context=True)
    #  dispatcher = updater.dispatcher
    #  start_handler = CommandHandler('start', start)
    #  dispatcher.add_handler(start_handler)
    #  updater.start_polling()
