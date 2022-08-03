import requests
import json
import telebot
import getcomm
with open(bytes('config.json',encoding='UTF-8')) as f: #读
    botJsonStr = json.load(f)
    botToken = botJsonStr['data'][0]['botToken']
    bot = telebot.TeleBot(botToken)
def getSfwPic(message):
        print("[setu.py]用户(ID:" + str(message.from_user.id) + ")发送SFW获取色图命令！")
        res=requests.get('https://api.lolicon.app/setu/v2/?r18=0')
        json_str=json.loads(res.text)
        print('[setu.py]已成功取到JSON')
        print('[setu.py]开始解析JSON数据')
        url=json_str['data'][0]['urls']['original']
        title=json_str['data'][0]['title']
        r18=json_str['data'][0]['r18']
        tags=json_str['data'][0]['tags']
        print("[setu.py]数据解析完毕，向用户发送数据")
        picinfo="[@MashiroLoliBot]图片信息:" + "\n" + "图片链接:" + str(url) + "\n" + "作品标题:" + str(title) + "\n" + "是否R18:" + str(r18) + "\n" + "作品标签:" + str(tags)
        bot.reply_to(message,picinfo)
def getNsfwPic(message):
        print("[setu.py]用户(ID:" + str(message.from_user.id) + ")发送获取NSFW色图命令！")
        res=requests.get('https://api.lolicon.app/setu/v2/?r18=1')
        json_str=json.loads(res.text)
        print('[setu.py]已成功取到JSON')
        print('[setu.py]开始解析JSON数据')
        url=json_str['data'][0]['urls']['original']
        title=json_str['data'][0]['title']
        r18=json_str['data'][0]['r18']
        tags=json_str['data'][0]['tags']
        pid=json_str['data'][0]['tags']
        print("[setu.py]数据解析完毕，向用户发送数据")
        picinfo="[@MashiroLoliBot]图片信息:" + "\n" + "图片链接:" + str(url) + "\n" + "作品标题:" + str(title) + "\n" + "是否R18:" + str(r18) + "\n" + "作品标签:" + str(tags)
        bot.reply_to(message,picinfo)
def searchSfwPic(message):
        userInputKey = getcomm.get_command_text(message.text)
        if userInputKey != False:
                ssfwpic_text = bot.reply_to(message,'正在搜索,请稍后....')
                print("[setu.py]用户(ID:" + str(message.from_user.id) + ")发送搜索SFW色图命令！" + '\n' + '[setu.py]关键词:' + userInputKey)
                res=requests.get('https://api.lolicon.app/setu/v2/?r18=0&keyword='+userInputKey)
                json_str=json.loads(res.text)
                print('[setu.py]已成功取到JSON')
                print('[setu.py]开始解析JSON数据')
                url=json_str['data'][0]['urls']['original']
                title=json_str['data'][0]['title']
                r18=json_str['data'][0]['r18']
                tags=json_str['data'][0]['tags']
                print("[setu.py]数据解析完毕，向用户发送数据")
                picinfo="[@MashiroLoliBot]图片信息:" + "\n" + "图片链接:" + str(url) + "\n" + "作品标题:" + str(title) + "\n" + "是否R18:" + str(r18) + "\n" + "作品标签:" + str(tags)
                bot.edit_message_text(picinfo, ssfwpic_text.chat.id, ssfwpic_text.message_id)
def searchNsfwPic(message):
        userInputKey = getcomm.get_command_text(message.text)
        if userInputKey != False:
                snsfwpic_text = bot.reply_to(message,'正在搜索,请稍后....')
                print("[setu.py]用户(ID:" + str(message.from_user.id) + ")发送搜索NSFW色图命令！" + '\n' + '[setu.py]关键词:' + userInputKey)
                res=requests.get('https://api.lolicon.app/setu/v2/?r18=1&keyword='+userInputKey)
                json_str=json.loads(res.text)
                print('[setu.py]已成功取到JSON')
                print('[setu.py]开始解析JSON数据')
                url=json_str['data'][0]['urls']['original']
                title=json_str['data'][0]['title']
                r18=json_str['data'][0]['r18']
                tags=json_str['data'][0]['tags']
                print("[setu.py]数据解析完毕，向用户发送数据")               
                picinfo="[@MashiroLoliBot]图片信息:" + "\n" + "图片链接:" + str(url) + "\n" + "作品标题:" + str(title) + "\n" + "是否R18:" + str(r18) + "\n" + "作品标签:" + str(tags)
                bot.edit_message_text(picinfo, snsfwpic_text.chat.id, snsfwpic_text.message_id)
