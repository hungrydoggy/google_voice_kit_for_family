#-*- coding: utf-8 -*-
from module.fam import *


def main():
    number = getRandom(1, 3)   # 1 부터 3 까지 숫자 중 아무거나 뽑아서, number 변수에 넣어 놓는다

    if number == 1:        # number 가 1 이면
        playSound("cow")   # 소 소리를 재생

    if number == 2:        # number 가 2 이면
        playSound("duck")  # 오리 소리를 재생

    if number == 3:        # number 가 3 이면
        playSound("tiger") # 호랑이 소리를 재생


    waitButton()       # 플레이어가 버튼을 누를 때 까지 기다린다

    answer = listen()  # 플레이어가 외친 정답을 받아온다


    if number == 1 and answer == '소':     # number 가 1 이고, answer 가 '소' 이면 정답.
        print('정답 입니다')

    if number == 2 and answer == '오리':    # number 가 2 이고, answer 가 '오리' 이면 정답.
        print('정답 입니다')

    if number == 3 and answer == '호랑이':   # number 가 3 이고, answer 가 '호랑이' 이면 정답.
        print('정답 입니다')

    print('...')


run(main)

