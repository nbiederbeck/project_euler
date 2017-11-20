import telepot
token = '394103686:AAHlJUxbqtfCm92XklUlmU2jTRU2uTqvwUI'
chatid = 322086570
bot = telepot.Bot(token)
def message(text):
    if type(text)==str:
       bot.sendMessage(chat_id=chatid, text=text)
    else:
        print('WARNING: message must be string-type!')
