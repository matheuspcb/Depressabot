import telebot

tk = "7143926859:AAFbvSXqe_2rQMrFl7FF8cQZtOsYjNggdJI"

bot = telebot.TeleBot(tk)

@bot.message_handler(commands=["start", "ola", "oi"])

def primeira_msg(message):

    id = message.chat.id

    bot.send_message(id, "Olá amigo")

bot.polling()
