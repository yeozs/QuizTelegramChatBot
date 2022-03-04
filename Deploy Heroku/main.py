#https://www.youtube.com/watch?v=bu5wXjz2KvU => google sheet-python
#https://www.youtube.com/watch?v=ps1yeWwd6iA => python-telegram
#pip install gspread

import gspread #Google Spreadsheet library
import telebot #Telegram Bot Library
import urllib #URI encode Data for URL
import requests #send POST request to telegram
import schedule
import time



#------------------------ Google Sheet Side (Extract Data)
serviceAccount = gspread.service_account(filename="<INSERT JSON FILE HERE BLABLA.JSON>")
sheets = serviceAccount.open("ACS_Weekly_Quiz_Bot")

cqrWorksheet = sheets.worksheet("Code")
completeQuizReminder = cqrWorksheet.acell('A2').value

corWorksheet = sheets.worksheet("QuizOpenReminder")
quizOpenReminder = corWorksheet.acell('D23').value

#------------------------ Telegram Bot Side (Send Data)
TOKEN = '<INSERT TELEBOT TOKEN HERE>'
chatId = '<INSERT TELEGRAM CHANNEL/GROUP ID HERE>'
telegramURL = "https://api.telegram.org/bot" + TOKEN
bot = telebot.TeleBot(token = TOKEN)
baseSendMessageURL = telegramURL + "/sendMessage?chat_id=" + chatId + "&text="


def quizReminderTrigger():
  text = str(urllib.parse.quote(completeQuizReminder))
  sendMessageURL = baseSendMessageURL + text + "&parse_mode=HTML"
  print(sendMessageURL)
  response = requests.post(sendMessageURL)


def quizOpenTrigger():
  text = str(urllib.parse.quote(quizOpenReminder))
  sendMessageURL = baseSendMessageURL + text + "&parse_mode=HTML"
  print(sendMessageURL)
  response = requests.post(sendMessageURL)
#--------------------------working code below
bot.set_webhook()
#quizReminderTrigger()
#quizOpenTrigger()

#schedule.every().thursday.at("14:35:00").do(quizOpenTrigger)
#schedule.every().friday.at("01:00:00").do(quizReminderTrigger)

schedule.every().sunday.at("04:00:00").do(quizOpenTrigger) #sunday 12pm quiz open
schedule.every().saturday.at("12:00:00").do(quizReminderTrigger) #saturday 9pm trigger message
while True: #while true
    schedule.run_pending() #run code that need to run
    time.sleep(1) #sleep 1 second