import logging
from telegram.ext import Updater, CommandHandler

# Запускаем логгирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Копируем токен бота
TOKEN = 'BOT_TOKEN'


# Функция приветствия пользователя
def start(update, context):
    # Поприветствуем пользователя
    update.message.reply_text("Привет, я фотошоп бот. Для ознакомления с моим функционалом напиши команду /help")


def help(update, context):
    update.message.reply_text("Пока что я балбес")


# Основная функция
def main():
    # Создаем объект updater
    updater = Updater(TOKEN)

    # Получаем из updater'а диспетчер сообщений
    dp = updater.dispatcher

    # Зарегистрируем 2 базовых команды в диспетчере
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Запускаем цикл приема и обработки сообщений
    updater.start_polling()

    # Ждем завершения приложения
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта
if __name__ == "__main__":
    main()
