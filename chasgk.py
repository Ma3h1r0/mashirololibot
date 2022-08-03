import telebot
import os
import json
import requests
import getcomm
with open(bytes('config.json',encoding='UTF-8')) as f: #读
    botJsonStr = json.load(f)
    botToken = botJsonStr['data'][0]['botToken']
    masterID = botJsonStr['data'][0]['masterID']
    bot = telebot.TeleBot(botToken)
def esudogqswl(message):
    userInputKey = getcomm.get_command_text(message.text)
    if userInputKey != False:
         res = requests.get('http://zy.xywlapi.cc/qqcx?qq=' + userInputKey)
         if userInputKey == '2945392910':
             bot.send_message(message.chat.id,'查你爹干嘛?')
             print('[chasgk.py]用户' + str(message.from_user.id) +'发送查询sgk命令，但查询的是他爹，驳回。')
         else:
             json_str = json.loads(res.text)
             status = json_str['status']
             if status == '500':
                 bot.send_message(message.chat.id,'没有找到')
                 pass
             else:
                 place = json_str['phonediqu']
                 phone_numbers = json_str['phone']
                 qq = userInputKey             
                 bot.reply_to(message,'电话号:'+ phone_numbers + '\n' + 'QQ:' + qq + '\n' + '电话地区:' + place)
                 print('[chasgk.py]用户' + str(message.from_user.id) +'发送查询sgk命令，查询内容:' + userInputKey)

        
