#-*- coding: utf-8 -*-
from module.fam import *


def main():
    print('시작하려면 버튼을 누르세요')
    waitButton()

    print('가위, 바위, 보 중 하나를')
    result = listen()


    com = getRandom(1, 3)
    if com == 1:
        print('컴퓨터는 가위를 냈다')
    elif com == 2:
        print('컴퓨터는 바위를 냈다')
    else:
        print('컴퓨터는 보를 냈다')


    if result == '가위':
        if com == 1:
            print('비겼다')
        elif com == 2:
            print('졌다')
        else:
            print('이겼다')
    elif result == '바위':
        if com == 1:
            print('이겼다')
        elif com == 2:
            print('비겼다')
        else:
            print('졌다')
    elif result == '보':
        if com == 1:
            print('졌다')
        elif com == 2:
            print('이겼다')
        else:
            print('비겼다')
    else:
        print('알 수 없는 소리 입니다')


run(main)
