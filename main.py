import telebot
from telebot import types
import requests
import json
import os
import re
import os.path
import setu
import loli_helpcommand
import keyword_reply as lol
import chasgk
print(f"[main.py]开始初始化")
print(f"[main.py]加载配置文件")
with open(bytes('config.json',encoding='UTF-8')) as f: #读
    botJsonStr = json.load(f)
    botToken = botJsonStr['data'][0]['botToken']
    masterID = botJsonStr['data'][0]['masterID']
    print(f"[main.py]您配置的botToken为:"+botToken+",主人ID为:"+masterID+"请检查是否正确！")
    bot = telebot.TeleBot(botToken)
    print(f"[main.py]配置文件加载完毕!")
    bot.send_message(masterID,"报告主人，我已上线！")
@bot.message_handler(commands=['sfw','来点涩图'])
def sendSfwPic(message):
        setu.getSfwPic(message)
        bot.send_chat_action(message.chat.id,'typing')
@bot.message_handler(commands=['nsfw','来点色图'])
def sendNsfwPic(message):
        setu.getNsfwPic(message)
        bot.send_chat_action(message.chat.id,'typing')
@bot.message_handler(commands=['搜索涩图','ssfw'])
def sendSSfwPic(message):
        setu.searchSfwPic(message)
        bot.send_chat_action(message.chat.id,'typing')
@bot.message_handler(commands=['搜索色图','snsfw'])
def sendSNsfwPic(message):
        setu.searchNsfwPic(message)
        bot.send_chat_action(message.chat.id,'typing')
@bot.message_handler(commands=['help','start'])
def sendHelpCommand(message):
        loli_helpcommand.sendWelcome(message)
        bot.send_chat_action(message.chat.id,'typing')
@bot.message_handler(commands=['sgk','查q绑'])
def esudog(message):
            chasgk.esudogqswl(message)
            bot.send_chat_action(message.chat.id,'typing')
@bot.message_handler()
def xswl(message,keyword='傻逼',reply_message='你说话怎么这么难听啊我靠？'):
        lol.keyword_reply(message,keyword,reply_message)
        bot.send_chat_action(message.chat.id,'typing')
    
#let bot polling
bot.infinity_polling()
