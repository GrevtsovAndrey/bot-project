import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from PIL import Image, ImageDraw


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

    # @bot.message_handler(content_types=['photo', 'document'])
# def download_image(message):
    # from pathlib import Path
    # Path(f'files/{message.chat.id}/').mkdir(parents=True, exist_ok=True)
    # if message.content_type == 'photo':
        # file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        # downloaded_file = bot.download_file(file_info.file_path)
        # src = f'files/{message.chat.id}/' + file_info.file_path.replace('photos/', '')
        # with open(src, 'wb') as new_file:
            # new_file.write(downloaded_file)


    # elif message.content_type == 'document':
        # file_info = bot.get_file(message.document.file_id)
        # downloaded_file = bot.download_file(file_info.file_path)
        # src = f'files/{message.chat.id}/' + message.document.file_name
        # with open(src, 'wb') as new_file:
            # new_file.write(downloaded_file)


def get_image(update, context):
    global updater
    file_info = updater.bot.get_file(update.message.photo[-1])
    downloaded_file = updater.bot.download_file(file_info)
    src = ""
    with open(src, "wb") as new_file:
        new_file.write(downloaded_file)


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
    image_handler = MessageHandler(Filters.document.image & (~Filters.command), get_image)
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
