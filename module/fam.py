#-*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time, os



def ledOn ():
    gpio.output(kLed, 1)

def ledOff ():
    gpio.output(kLed, 0)

def sleep (sec):
    time.sleep(sec)

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
    os.system("omxplayer -o alsa %s" % path)


kLed = 25
kButton = 23

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(kLed, gpio.OUT)
    gpio.setup(kButton, gpio.IN)

def shutdown():
    gpio.cleanup()

def run(func):
    init()

    try:
        func()
    except Exception as e:
        shutdown()
        raise e

    shutdown()

