import logging

from telegram import ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import requests

from PIL import Image

# Запускаем логгирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Копируем токен бота
TOKEN = "5294422299:AAG8VQO8dV3thi-DE1UCNREFrI82NCVy3qY"

# Создадим стартовую клавиатуру


# Функция удаления клавиатуры
def close_keyboard(update, context):
    update.message.reply_text("Ok", reply_markup=ReplyKeyboardRemove())


# Функция приветствия пользователя
def start(update, context):
    update.message.reply_text("Привет, я фотошоп бот. Для ознакомления с моим функционалом напиши команду /help")


def help(update, context):
    update.message.reply_text("Пока что я балбес")


def get_image(update, context):
    picture = update.message.photo[-1]
    file = picture.file_id
    obj = context.bot.get_file(file)
    file_path = obj.file_path
    response = requests.get(file_path)
    out = open("telegram_image.jpg", "wb")
    out.write(response.content)
    out.close()


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
    # Создаем объект updater
    updater = Updater(TOKEN)

    # Получаем из updater'а диспетчер сообщений
    dp = updater.dispatcher

    # Создаем обработчики
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)
    image_handler = MessageHandler(Filters.photo, get_image)
    close_keyboard_handler = CommandHandler("close", close_keyboard)
    turn_right_handler = CommandHandler("turn_right", turn_right)
    turn_left_handler = CommandHandler("turn_left", turn_left)
    flip_vertical_handler = CommandHandler("flip_vertical", flip_vertical)
    flip_horizontally_handler = CommandHandler("flip_horizontally", flip_horizontally)
    compression_handler = CommandHandler("compression", compression)
    effect_handler = CommandHandler("3D_effect", getting_the_3D_effect)

    # Регистрируем обработчики
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)
    dp.add_handler(image_handler)
    dp.add_handler(close_keyboard_handler)
    dp.add_handler(turn_right_handler)
    dp.add_handler(turn_left_handler)
    dp.add_handler(flip_vertical_handler)
    dp.add_handler(flip_horizontally_handler)
    dp.add_handler(compression_handler)
    dp.add_handler(effect_handler)

    # Создадим клавиатуру для выбора одной из команд

    # Запускаем цикл приема и обработки сообщений
    updater.start_polling()

    # Ждем завершения приложения
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта
if __name__ == "__main__":
    main()
