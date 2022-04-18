import logging

from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import requests

from PIL import Image

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
                      ["/flip_vertical", "/flip_horizontally"],
                      ["/white_black", "/3D_effect"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    update.message.reply_text("Для начала работы или изменения фото отправте его, \n"
                              "Список команд: \n"
                              "/turn_right - поворот вправо \n"
                              "/turn_left - поворот влево \n"
                              "/flip_vertical - отаржение по вертикали \n"
                              "/flip_horizontally - отражение по горизонтали \n"
                              "/while_black - черно-белый эффект \n"
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
                      ["/flip_vertical", "/flip_horizontally"],
                      ["/white_black", "/3D_effect"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    update.message.reply_text("Изображение успешно получено",
                              reply_markup=markup)


def turn_right(update, context):
    im = Image.open("telegram_image.jpg")
    im.transpose(Image.ROTATE_270).save('telegram_image.jpg')
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


def turn_left(update, context):
    im = Image.open("telegram_image.jpg")
    im.transpose(Image.ROTATE_90).save('telegram_image.jpg')
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


def flip_vertical(update, context):
    im = Image.open("telegram_image.jpg")
    pix_s = im.load()
    x, y = im.size
    for i in range(x // 2):
        for j in range(y):
            pix_s[i, j], pix_s[x - i - 1, j] = pix_s[x - i - 1, j], pix_s[i, j]
    im.save("telegram_image.jpg")
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


def flip_horizontally(update, context):
    im = Image.open("telegram_image.jpg")
    pix_s = im.load()
    x, y = im.size
    for i in range(x // 2):
        for j in range(y):
            pix_s[i, j], pix_s[x - i - 1, j] = pix_s[x - i - 1, j], pix_s[i, j]
    im.transpose(Image.ROTATE_180).save('telegram_image.jpg')
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


def white_black(update, context):
    im = Image.open("telegram_image.jpg")
    pix_s = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pix_s[i, j]
            bw = (r + g + b) // 3
            pix_s[i, j] = bw, bw, bw
    im.save("telegram_image.jpg")
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


def getting_the_3D_effect(update, context):
    delta = 8
    im = Image.open("telegram_image.jpg")
    x, y = im.size
    imR = im.copy()
    pixR = imR.load()
    for i in range(x):
        for j in range(y):
            r = list(pixR[i, j])[0]
            pixR[i, j] = (r, 0, 0)
    imGB = im.copy()
    pixGB = imGB.load()
    for i in range(x):
        for j in range(y):
            g = list(pixGB[i, j])[1]
            b = list(pixGB[i, j])[2]
            pixGB[i, j] = (0, g, b)
    for i in range(x):
        for j in range(y):
            if i - delta >= 0:
                r, g, b = pixGB[i, j]
                R = list(pixR[i - delta, j])[0]
                pixGB[i, j] = (r + R, g, b)
    im = imGB.copy()
    im.save("telegram_image.jpg")
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


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
    turn_right_handler = CommandHandler("turn_right", turn_right)
    turn_left_handler = CommandHandler("turn_left", turn_left)
    flip_vertical_handler = CommandHandler("flip_vertical", flip_vertical)
    flip_horizontally_handler = CommandHandler("flip_horizontally", flip_horizontally)
    white_black_handler = CommandHandler("white_black", white_black)
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
    dp.add_handler(white_black_handler)
    dp.add_handler(effect_handler)

    # Создадим клавиатуру для выбора одной из команд

    # Запускаем цикл приема и обработки сообщений
    updater.start_polling()

    # Ждем завершения приложения
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта
if __name__ == "__main__":
    main()
