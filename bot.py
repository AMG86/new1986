import logging
# импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename = 'bot.log', level = logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

# Вызов функции при старте
def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота.
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs = PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

'''if __nane__ == "__main__":
    main()'''

main()
