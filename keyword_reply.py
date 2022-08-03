import telebot
from telebot import types
import json
import re
with open(bytes('config.json',encoding='UTF-8')) as f: #读
    botJsonStr = json.load(f)
    botToken = botJsonStr['data'][0]['botToken']
    masterID = botJsonStr['data'][0]['masterID']
    bot = telebot.TeleBot(botToken) 
@bot.message_handler()
def keyword_reply(message,keyword,reply_message):
    result_key = re.search(keyword,message.text)
    if result_key != None:
        if result_key.group() == keyword:
             bot.send_message(message.chat.id,reply_message)
        else:
            print('[keyword_reply.py]用户发送信息: ' + message.text + '(没有找到对应KEYWORD，不回复)')
            pass
