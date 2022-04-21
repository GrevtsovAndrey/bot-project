# Импортируем нужные библиотеки и файл с функциями

import image_functions

import logging

from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import requests


# Запускаем логгирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Копируем токен бота
TOKEN = "5294422299:AAG8VQO8dV3thi-DE1UCNREFrI82NCVy3qY"


# Функция удаления клавиатуры
def close_keyboard(update, context):
    update.message.reply_text("Ok", reply_markup=ReplyKeyboardRemove())


# Функция приветствия пользователя
def start(update, context):
    reply_keyboard = [["/help"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    update.message.reply_text("Привет, я фотошоп бот. Для ознакомления с моим функционалом напиши команду /help",
                              reply_markup=markup)


# Ознакомительная функция
def help(update, context):
    # Клавиатура с функциями
    reply_keyboard = [["/turn_right", "/turn_left"],
                      ["/flip_vertical", "/flip_horizontally", "/reflection_diagonally"],
                      ["/white_black", "/blur", "/3D_effect"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    update.message.reply_text("Для начала работы или изменения фото отправте его, \n"
                              "Список команд: \n"
                              "/turn_right - поворот вправо \n"
                              "/turn_left - поворот влево \n"
                              "/flip_vertical - отаржение по вертикали \n"
                              "/flip_horizontally - отражение по горизонтали \n"
                              "/reflection_diagonally - отражение по горизонтали \n"
                              "/while_black - черно-белый эффект \n"
                              "/blur - размытие изображения \n"
                              "/3D_effect - получение 3D эффекта",
                              reply_markup=markup)


# Функция получения изображения
def new_image(update, context):
    picture = update.message.photo[-1]
    file = picture.file_id
    obj = context.bot.get_file(file)
    file_path = obj.file_path
    response = requests.get(file_path)
    out = open("telegram_image.jpg", "wb")
    out.write(response.content)
    out.close()
    # Создаем клавиатуру
    reply_keyboard = [["/turn_right", "/turn_left"],
                      ["/flip_vertical", "/flip_horizontally", "/reflection_diagonally"],
                      ["/white_black", "/blur", "/3D_effect"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    update.message.reply_text("Изображение успешно получено",
                              reply_markup=markup)


# Основная функция
def main():
    # Создаем объект updater
    updater = Updater(TOKEN)

    # Получаем из updater'а диспетчер сообщений
    dp = updater.dispatcher

    # Создаем обработчики
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)
    image_handler = MessageHandler(Filters.photo, new_image)
    close_keyboard_handler = CommandHandler("close", close_keyboard)
    turn_right_handler = CommandHandler("turn_right", image_functions.turn_right)
    turn_left_handler = CommandHandler("turn_left", image_functions.turn_left)
    flip_vertical_handler = CommandHandler("flip_vertical", image_functions.flip_vertical)
    flip_horizontally_handler = CommandHandler("flip_horizontally", image_functions.flip_horizontally)
    reflection_diagonally_handler = CommandHandler("reflection_diagonally", image_functions.reflection_diagonally)
    white_black_handler = CommandHandler("white_black", image_functions.white_black)
    blur_handler = CommandHandler("blur", image_functions.blur)
    effect_handler = CommandHandler("3D_effect", image_functions.getting_the_3D_effect)

    # Регистрируем обработчики
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)
    dp.add_handler(image_handler)
    dp.add_handler(close_keyboard_handler)
    dp.add_handler(turn_right_handler)
    dp.add_handler(turn_left_handler)
    dp.add_handler(flip_vertical_handler)
    dp.add_handler(flip_horizontally_handler)
    dp.add_handler(reflection_diagonally_handler)
    dp.add_handler(white_black_handler)
    dp.add_handler(blur_handler)
    dp.add_handler(effect_handler)

    # Создадим клавиатуру для выбора одной из команд

    # Запускаем цикл приема и обработки сообщений
    updater.start_polling()

    # Ждем завершения приложения
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта
if __name__ == "__main__":
    main()
