#-*- coding: utf-8 -*-
from module.fam import *
import sys

if len(sys.argv) >= 2:
    code_path = sys.argv[1]
else:
    code_path = "code.py"

init()

try:
    #execfile('code.py')
    exec(open(code_path).read())
except Exception as e:
    shutdown()
    raise e

shutdown()
