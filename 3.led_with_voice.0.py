#-*- coding: utf-8 -*-
from module.fam import *


def main():
    result = listen()
    if result == 'LED 켜기':
        ledOn()
        sleep(1)
        ledOff()
        sleep(1)



run(main)
