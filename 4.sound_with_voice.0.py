#-*- coding: utf-8 -*-
from module.fam import *


def main():
    result = listen()
    if result == '소':
        playSound('cow')
    elif result == '오리':
        playSound('duck')
    elif result == '호랑이':
        playSound('tiger')
    else:
        print('알 수 없는 소리 입니다')


run(main)
