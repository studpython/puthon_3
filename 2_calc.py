# -*- coding: utf-8 -*-

def add(a,b):
    print(a+b)
def min(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def split(a,b):
    print(a/b)

print('input calculator operation')
print('example: 11 + 22')
done = True
while done:
    line = input()
    mas = line.split()
    a = int(mas[0])
    b = mas[1]
    c = int(mas[2])
    if b == '+':
        add(a,c)
    elif b == '-':
        min(a,c)
    elif b == '*':
        mult(a,c)
    elif b == '/':
        if c == int(0):
            print('null')
        split(a,c)
