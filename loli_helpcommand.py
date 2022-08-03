import telebot
import json
with open(bytes('config.json',encoding='UTF-8')) as f: #读
    botJsonStr = json.load(f)
    botToken = botJsonStr['data'][0]['botToken']
    masterID = botJsonStr['data'][0]['masterID']
    bot = telebot.TeleBot(botToken)
def sendWelcome(message):
    print('[loli_helpcommand.py]用户(ID:'+str(message.from_user.id)+")发送了一个help command")
    bot.reply_to(message, "你好！我是@LoliMashiro的机器人\n"+"Command List:\n"+"/sfw 获取涩图\n"+"/nsfw 获取色图\n"+"/搜索涩图 Keyword 搜索SFW涩图\n"+"/搜索色图 Keyword 搜索NSFW色图" )
#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
    

#bot.infinity_polling()
