import telebot

# Crie uma instância do bot
bot = telebot.TeleBot('5744881902:AAF7Q0tUmWgN9OOE_NWCXeua58nFrMvBOXQ')

@bot.message_handler(commands=['delete'])
def delete_message(message):
    # Exclua a mensagem enviada pelo usuário
    bot.delete_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)

# Inicie o bot
bot.polling()
