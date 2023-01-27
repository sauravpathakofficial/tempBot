import requests
import time
import telebot

# will hide these keys in env file in future 
BOT_TOKEN = "5957042827:AAHlt0NSnnNBocK29Ltsyz9xfH_gKt3RFqI"
# API_key="970fc6a39a0024a3747f61f399c15651"

bot = telebot.TeleBot(BOT_TOKEN)

def get_data():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=970fc6a39a0024a3747f61f399c15651')
    data = response.json()
    return data

def format_message():
    data=get_data()
    weather=data['weather'][0]['main']
    curr_temp=round(data['main']['temp']-273.15,2)
    mintemp=round(data['main']['temp_min']-273.15,2)
    maxtemp=round(data['main']['temp_max']-273.15,2)
    result="The Weather in Delhi : "+ weather +"\n"+"Current Temperature is "+ format(curr_temp) +"\n"+"with a low temperature of "+ format(mintemp) +" and high of "+ format(maxtemp)
    return result

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hey! Hows it going? call /temperature for temperature update at delhi for every hour ")

@bot.message_handler(commands=['temperature'])
def send_temp(message):
    while True:
        finalMessage=format_message()
        bot.send_message(message.chat.id, finalMessage)
        time.sleep(600)  # calling it every 10 minutes to check, will change it to 3600 for calling it every hour afterwards  

bot.polling()        


#  run first pip install pyTelegramBotAPI 
# run pip install requests
# open https://web.telegram.org/k/#@delhitempbot 