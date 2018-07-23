#-*- coding: utf-8 -*-
from module.fam import *


def main():
    number = getRandom(1, 3)

    if number == 1:
        playSound("cow")

    if number == 2:
        playSound("duck")

    if number == 3:
        playSound("tiger")


run(main)

