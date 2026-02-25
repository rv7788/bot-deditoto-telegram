import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "7756732275:AAHNgUUfKyxJR6ZHNanJaW21X7d8PTbGK84"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    keyboard = InlineKeyboardMarkup()

    # Baris 1
    keyboard.row(
        InlineKeyboardButton("📢 Join Channel 1", url="https://t.me/asupanviral2026"),
        InlineKeyboardButton("📢 Join Channel 2", url="https://t.me/asupanvideyhariini")
    )

    # Baris 2
    keyboard.row(
        InlineKeyboardButton("📢 Join Channel 3", url="https://t.me/nontonvideygratis"),
        InlineKeyboardButton("📢 Join Channel 4", url="https://t.me/nontonvideygratis")
    )

    bot.send_message(
        message.chat.id,
        "Silakan pilih channel yang ingin kamu join:",
        reply_markup=keyboard
    )


bot.polling()