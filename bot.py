import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "7756732275:AAHNgUUfKyxJR6ZHNanJaW21X7d8PTbGK84"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    keyboard = InlineKeyboardMarkup()

    # Baris 1
    keyboard.row(
        InlineKeyboardButton("Link Login", url="https://dedi88.com"),
        InlineKeyboardButton("RTP", url="https://t.ly/deditotortp")
    )

    # Baris 2
    keyboard.row(
        InlineKeyboardButton("Whatsapp Official", url="https://api.whatsapp.com/send/?phone=6287790595197&text&type=phone_number&app_absent=0"),
        InlineKeyboardButton("Google", url="https://www.google.com/search?q=dedi+toto&sca_esv=4b6fd4b69e4fa74a&sxsrf=ANbL-n5qKcVPg19LtglBZhhy1cGGswx1wA%3A1772000751360&ei=75Weacv2FMaUg8UP1Nnx4QE&biw=1920&bih=945&ved=0ahUKEwiLqs2agfSSAxVGyqACHdRsPBwQ4dUDCBE&uact=5&oq=dedi+toto&gs_lp=Egxnd3Mtd2l6LXNlcnAiCWRlZGkgdG90bzIEECMYJzIHEAAYgAQYCjIGEAAYCBgeMgYQABgIGB5I5gJQ4gFY4gFwAXgAkAEAmAE4oAE4qgEBMbgBA8gBAPgBAZgCAaACPJgDAIgGAZIHATGgB9IDsgcBMbgHPMIHAzAuMcgHAoAIAA&sclient=gws-wiz-serp")
    )

    bot.send_message(
        message.chat.id,
        "Halo Bossku Ada yang bisa DEDITOTO bantu?",
        reply_markup=keyboard
    )



bot.polling()
