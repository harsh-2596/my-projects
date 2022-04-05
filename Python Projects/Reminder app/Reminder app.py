# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Please the add these files to your current directory as well

import schedule
import time
import datetime
from pygame import mixer


def audio(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    noww = datetime.datetime.now()
    with open("mylogs.txt", "a") as tt:
        tt.write(f"{msg} {noww.strftime('%a %d %b,%Y %H:%M:%S')} \n")


def reminder():
    init_water = time.time()
    init_eyes = time.time()
    init_exer = time.time()
    wsec = 30 * 60
    eysec = 32 * 60
    exsec = 40 * 60
    while True:
        if time.time() - init_water > wsec:
            print("Do You Know What Time It is??, \n"
                  "It's time to Drink Some Water\n"
                  "Make Sure You Drink At least 200 ml")
            print("Press 'Q' to stop the alarm")
            audio("water.mp3", "Q")
            init_water = time.time()
            log_now("Drank Water at : ")
        if time.time() - init_eyes > eysec:
            print("It's time to relax Your Eyes and Mind\n"
                  "Make Sure You close your eyes For 5 Minutes \n"
                  "Wash your Face as well")
            print("Press 'Q' to stop the alarm")
            audio("eyes.mp3", "Q")
            init_eyes = time.time()
            log_now("Relaxed Eyes at : ")
        if time.time() - init_exer > exsec:
            print("It's time to move Your Body\n"
                  "Stand Up And Walk through Your Room\n"
                  "Stretch out All of Your Muscles")
            print("Press 'Q' to stop the alarm")
            audio("exercise.mp3", "Q")
            init_exer = time.time()
            log_now("Exercise Done at : ")


schedule.every().day.at("09:00").until("20:00").do(reminder)
while 1:
    schedule.run_pending()
    time.sleep(0)
