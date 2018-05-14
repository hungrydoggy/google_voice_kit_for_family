#-*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time, os, sys, random
import speech_recognition as sr  

from module.key import wit_access_token
from module.no_err import noalsaerr



def ledOn ():
    gpio.output(kLed, 1)

def ledOff ():
    gpio.output(kLed, 0)

def sleep (sec):
    time.sleep(sec)

def getRandom (first=0, last=100):
    return random.randint(first, last)

def waitButton (info_str = "버튼을 누르세요"):
    print(info_str)

    # wait button off
    while True:
        if gpio.input(kButton) == 1:
            break
        time.sleep(0.1)

    # wait button on
    while True:
        if gpio.input(kButton) == 0:
            break
        time.sleep(0.1)

def playSound (name):
    path = './sounds/%s.mp3' % name
    if os.path.exists(path) == False:
        raise(Exception('\"%s\"를 찾을 수 없습니다. 스펠링을 확인하세요.' % path))
    print('\"%s.mp3\"를 재생합니다' % name)
    os.system("omxplayer -o alsa %s > /dev/null" % path)

def listen ():
    #r.pause_threshold = 0.8

    while True:
        with noalsaerr() as n, sr.Microphone() as source:  
                print("말하세요!")  
                audio = recognizer.listen(source)  

        # recognize speech using wit.ai
        print("인식중 입니다...")
        try:  
            result = recognizer.recognize_wit(audio, wit_access_token)
            print("인식된 내용: '" + result + "'")  
            return result
        except sr.UnknownValueError:  
            print("인식할 수 없습니다.")  
        except sr.RequestError as e:  
            print("에러 발생: %s" % e)  


kLed = 25
kButton = 23

recognizer = None

def init ():
    gpio.setmode(gpio.BCM)
    gpio.setup(kLed, gpio.OUT)
    gpio.setup(kButton, gpio.IN)

    ledOff()

    # obtain audio from the microphone  
    global recognizer;
    recognizer = sr.Recognizer()  

    with noalsaerr() as n, sr.Microphone() as source:  
        os.system('clear')

def shutdown ():
    ledOff()
    gpio.cleanup()

def run (func):
    init()

    try:
        func()
    except Exception as e:
        shutdown()
        raise e

    shutdown()

