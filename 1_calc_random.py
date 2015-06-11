# -*- coding: utf-8 -*-

import random

done = True
while done:
    a = random.randint(0,1000)
    b = random.choice('+-*/')
    c = random.randint(0,100)
    if b == '+':
        print(a, '+', c, '=', a+c)
    elif b == '-':
        print(a, '-', c, '=', a-c)
    elif b == '*':
        print(a, '*', c, '=', a*c)
    elif b == '/':
        if c == int(0):
            print('null')
            break
        print(a, '/', c, '=', a/c)
