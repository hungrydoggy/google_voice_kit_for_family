#-*- coding: utf-8 -*-
from module.fam import *

init()

try:
    execfile('code.py')
except Exception as e:
    shutdown()
    raise e

shutdown()
