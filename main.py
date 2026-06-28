from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN") 
# TOKEN = 'TOKEN'  # replace with your bot token

def start(update, context):
    buttons = [[InlineKeyboardButton("Option 1", callback_data='1'), InlineKeyboardButton("Option 2", callback_data='2')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text('Hello, I am a bot. Choose an option:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    if query.data == '1':
        query.edit_message_text("You chose Option 1")
    elif query.data == '2':
        query.edit_message_text("You chose Option 2")

def echo(update, context):
    update.message.reply_text('Echo: {}'.format(update.message.text))

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    updater.start_polling()
    print('Bot started')
    updater.idle()

if __name__ == '__main__':
    main()

























































