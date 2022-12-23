#!/usr/bin/python3
"""Написать функцию. Для неё написать декораторы для следующего функционала:
    ◦ логирование выполнения функции;
    ◦ время выполнения функции;
    ◦ замедлить выполнение кода. Ограничить частоту вызова функции.
"""
import time

#время последнего запуска функции
last_start_func = 0

#декоратор логирования 
def logging(func):
    def wrapper():
        func()
        with open('log.txt', 'a') as file:
            file.write(f'{time.ctime()} Произошло логируемое выполнение функции\n')
    return wrapper

#декоратор времени выполнения
def timing(func):
    def wrapper():
        start = time.time()
        func()
        print(f'Время выполнения функции составило {time.time() - start} секунд')
    return wrapper


@logging
@timing
def another_func():
    print('Это та самая функция')

another_func()