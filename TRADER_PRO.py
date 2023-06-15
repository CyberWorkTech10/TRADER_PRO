import telebot
from telebot import types

chave = '5744881902:AAF7Q0tUmWgN9OOE_NWCXeua58nFrMvBOXQ'
bot = telebot.TeleBot(chave)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def inicio(mensagem):
    
    sim_botão = types.InlineKeyboardButton('Sim', callback_data='b_sim')
    nao_botão = types.InlineKeyboardButton('Não', callback_data='b_nao')

    inicial_keyboard = types.InlineKeyboardMarkup()
    inicial_keyboard.add(sim_botão, nao_botão)

    bot.send_message(mensagem.chat.id, 'Você deseja iniciar a configuração de sua conta?', reply_markup=inicial_keyboard)

    @bot.callback_query_handler(func=lambda call:True)
    def callback(call):
        chat_id = call.message.chat.id
#------------caminho do sim--------------#
        if call.data == 'b_sim':
            
            sim_botão_2 = types.InlineKeyboardButton('Sim', callback_data='b_sim_2')
            nao_botão_2 = types.InlineKeyboardButton('Não', callback_data='b_nao_2')

            back_time_keyboard = types.InlineKeyboardMarkup()
            back_time_keyboard.add(sim_botão_2, nao_botão_2)

            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text= 'Você deseja fazer as entradas do sinal segundos antes da abertura?', reply_markup=back_time_keyboard)

        if call.data == 'b_sim_2':
            
            botão_0s = types.InlineKeyboardButton('0 Segundo', callback_data='0_seg')
            botão_1s = types.InlineKeyboardButton('1 Segundo', callback_data='1_seg')
            botão_2s = types.InlineKeyboardButton('2 Segundo', callback_data='2_seg')
            botão_3s = types.InlineKeyboardButton('3 Segundo', callback_data='3_seg')

            back_time_sec_keyboard = types.InlineKeyboardMarkup()
            back_time_sec_keyboard.add(botão_0s, botão_1s, botão_2s, botão_3s)

            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text='Você pode escolher entre 0 e 3 segundos.', reply_markup=back_time_sec_keyboard)
            



bot.polling()



