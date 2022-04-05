import logging
from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from PIL import Image, ImageDraw

# Запускаем логгирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Копируем токен бота
TOKEN = 'BOT_TOKEN'

# Создадим стартовую клавиатуру
reply_keyboard = ["/help"]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

# Функция удаления клавиатуры
def close_keyboard(update, context):
    update.message.reply_text("Ok", reply_markup=ReplyKeyboardRemove())


# Функция приветствия пользователя
def start(update, context):
    global markup
    update.message.reply_text("Привет, я фотошоп бот. Для ознакомления с моим функционалом напиши команду /help",
                              reply_markup=markup)


def help(update, context):
    update.message.reply_text("Пока что я балбес")


def turn_right():
    pass


def turn_left():
    pass


def flip_vertical():
    pass


def flip_horizontally():
    pass


def compression():
    pass


def getting_the_3D_effect():
    pass


# Основная функция
def main():
    global markup
    # Создаем объект updater
    updater = Updater(TOKEN)

    # Получаем из updater'а диспетчер сообщений
    dp = updater.dispatcher

    # Зарегистрируем 2 базовых команды, команду закрытия клавиатуры и
    # основные команды для работы с картинками
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("turn_right", turn_right))
    dp.add_handler(CommandHandler("turn_left", turn_left))
    dp.add_handler(CommandHandler("flip_vertical", flip_vertical))
    dp.add_handler(CommandHandler("flip_horizontally", flip_horizontally))
    dp.add_handler(CommandHandler("compression", compression))
    dp.add_handler(CommandHandler("3D_effect", getting_the_3D_effect))

    # Создадим клавиатуру для выбора одной из команд
    reply_keyboard = [["/turn_right", "/turn_left"],
                      ["/flip_vertical", "/flip_horizontally"],
                      ["/compression", "/3D_effect"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    # Запускаем цикл приема и обработки сообщений
    updater.start_polling()

    # Ждем завершения приложения
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта
if __name__ == "__main__":
    main()
