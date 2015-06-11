# -*- coding: utf-8 -*-


import random

print('---Start---')
print('Привет! Я задумал случайное число от 1 до 100.')
print('У тебя есть 10 попыток чтоб угадать.')
a = random.randint(1, 100)
b = 0
#print(a)
while b < 10:
    b += 1
    print('--Попытка', b, 'Угадай, что я загадал:')
    c = int (input())
    if a < c:
        print('Слишком большое.')
        if b == 10:
            print('Оу, у тебя больше нет попыток. Загаданное число было', a)
            break
    elif a > c:
        print('Слишком маленькое.')
        if b == 10:
            print('Оу, у тебя больше нет попыток. Загаданное число было', a)
            break
    elif a == c:
        print('Ти угадал. Ура!!!')
        break
print('---End---')
        
