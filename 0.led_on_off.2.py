#-*- coding: utf-8 -*-
from module.fam import *


def main():
    for i in range(5):
        ledOn()
        sleep(0.3)
        ledOff()
        sleep(0.3)


run(main)
