#Controlling Raspberry Pi with Telegram
#Step:1.Open Terminal
#-> cd desktop
#->mkdir Telegram
#-> cd Telegram
#->sudo apt install python3-pip
#->sudo pip install telepot
#Step:2.Open Geany/Theny IDE
#->Write a code

import time
import datetime
import RPi.GPIO as GPIO
import telepot
import sys

def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return "Pin {} turned ON".format(pin)

def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return "Pin {} turned OFF".format(pin)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command: %s' % command)
    if command == 'on':
        bot.sendMessage(chat_id, on(11))
    elif command == 'off':
        bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('5329577491:AAHhKMS0XTk-H2DMAVMwI69hoN9vWXVGKfk')
bot.message_loop(handle)
print("I am Listening....")

while True:
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print('/ program interrupt')
        GPIO.cleanup()
        exit()
    except Exception as e:
        print('other error or exception occurred: {}'.format(e))
        GPIO.cleanup()

        
#Step:3.Open telegram in Smartphone
#->Search for Bot father->Click on Verified account
#->Open Bot->/Start
#->Name the Bot
#->Username of Bot
#->Copy Token Id to the code
#bot = telegram.bot('Token Id')
#Step:4.To run the Practical
#->Open terminal
#->cd ...path of code
#->python3 filename.py
#Step:5.Open Your Telegram Bot
#->on
#->off
