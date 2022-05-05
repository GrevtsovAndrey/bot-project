# Импортируем нужную библиотеки

from PIL import Image, ImageFilter


# Поворот вправо
def turn_right(update, context):
    im = Image.open("telegram_image.jpg")
    im = im.transpose(Image.ROTATE_270)
    im.save("telegram_image.jpg")
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


# Поворот влево
def turn_left(update, context):
    im = Image.open("telegram_image.jpg")
    im = im.transpose(Image.ROTATE_90)
    im.save("telegram_image.jpg")
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


# Отражение по вертикали
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


# Отражение по горизонтали
def flip_horizontally(update, context):
    im = Image.open("telegram_image.jpg")
    pix_s = im.load()
    x, y = im.size
    for i in range(x // 2):
        for j in range(y):
            pix_s[i, j], pix_s[x - i - 1, j] = pix_s[x - i - 1, j], pix_s[i, j]
    im = im.transpose(Image.ROTATE_180)
    im.save("telegram_image.jpg")
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


# Отражение по диагонали
def reflection_diagonally(update, context):
    im = Image.open("telegram_image.jpg")
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im = im.transpose(Image.ROTATE_270)
    im.save("telegram_image.jpg")
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


# Черно-белые эффект
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


# Размытие
def blur(update, context):
    im = Image.open("telegram_image.jpg")
    im = im.filter(ImageFilter.GaussianBlur(radius=5))
    im.save("telegram_image.jpg")
    id = update.message.chat.id
    context.bot.send_photo(chat_id=id, photo=open("telegram_image.jpg", "rb"))


# 3D еффект
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
