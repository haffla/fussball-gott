import os
import telegram

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
