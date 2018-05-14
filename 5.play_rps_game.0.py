#-*- coding: utf-8 -*-
from module.fam import *


def main():
    print('시작하려면')
    waitButton()


    com = getRandom(1, 3)
    if com == 1:
        print('컴퓨터는 가위를 냈다')
    elif com == 2:
        print('컴퓨터는 바위를 냈다')
    else:
        print('컴퓨터는 보를 냈다')

run(main)
