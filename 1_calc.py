# -*- coding: utf-8 -*-

done = True
while done:
    print ('input 1 number')
    a = int (input())
    print ('input +-*/**// or q for exit')
    b = input ()
    if b == 'q':
        break
    print ('input 2 number')
    c = int (input())
    if b == '+':
        print (a+c)
    elif b == '-':
        print (a-c)
    elif b == '*':
        print (a*c)
    elif b == '**':
        print (a**c)
    elif b == '/' or b == '//':
        if c == int(0):
            print ('null')
        elif b == '/':
            print (a/c)
        elif b == '//':
            print (a//c)
