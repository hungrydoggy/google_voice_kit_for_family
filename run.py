#-*- coding: utf-8 -*-
from module.fam import *

init()

try:
    #execfile('code.py')
    exec(open("code.py").read())
except Exception as e:
    shutdown()
    raise e

shutdown()
