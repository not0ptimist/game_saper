# -*- coding: utf-8 -*-
"""
Игра сапер, указываем число.
Функции формируют минное поле, и выводят чистое поле.
Вводим координаты, и смотрим результат.
"""
import datetime
import numpy as np

from lib.circle_find import circle_find
from lib.connect_db import conn_db


def construct_bombs(bomb):# Конструктор поля с минами
    all_field = bomb ** 2# Длина поля
    zeros = np.zeros((all_field), dtype=np.int)
    zeros[:bomb] = 1# Заполняем первую "строчку", мнимого квадратного поля
    np.random.shuffle(zeros)
    zeros = zeros.tolist()# При добавлении в базу ругается на тип np.ndarray
    print(zeros)# Указан для лучшего тестирования, в продакшене убрать
    return zeros


def construct_field(razmer):# Конструктор поля отображения игроку
    alpha = [chr(alpha) for alpha in range(65, 89)]# Список алфавита
    spisok = ['0' for x in range(razmer)]# Основное поле
    matrix = [list(alpha[x]) for x in range(razmer)]# Формирование столбца букв, стобец "x"
    for i in range(razmer):
        matrix[i].extend(spisok)# Добавление полей к столбцу
    matrix.insert(0, [str(x) for x in range(razmer + 1)])# Добавление верхней строки цифр, строка "y"
    return matrix


def proverka(x, y, osnov_arg, con_bomb):# Проверка координат на мину
    """Проверка на бомбу"""
    tochka = osnov_arg * (x - 65) + (int(y) - 1)
    print(con_bomb, tochka)
    if con_bomb[tochka] == 1:
        return False
    else:
        return True


def podskazka(x, y, con_bomb, con_field):# Вывод кол-ва мин
    razmer = len(con_field) - 1
    tochka = razmer * (x - 65) + (int(y) - 1)
    x = x - 64
    y = int(y)
    num_bomb = circle_find(tochka, con_bomb, razmer)# Подсчет ближайших мин
    con_field[x][y] = str(num_bomb)# Вписываем в указанную клетку число мин
    return con_field


def vvod_ploshadi():
    """
    Проверка получаемого значения для основных расчетов.
    Проблемы отображения при значении более 10
    """
    text_vvoda = 'Введите число для расчета площади и кол-ва мин, по умолчанию значение 6: '
    while True:
        osnov_arg = input(f'{text_vvoda}') or '6'
        if osnov_arg.isnumeric() and (6 <= int(osnov_arg) < 11):# Проверка на число
            break
        elif osnov_arg == 'exit':
            break
        else:
            print('Ввод неверного значения, повторите. Для выхода введите "exit".')
            continue
    return osnov_arg


def vivod_poly(con_field):
    """
    Вывод текущего поля.
    Переписана в функцию для последующего его модернизации,
    или другого отображения.
    """
    for i in con_field:
        for j in i:
            print(j, end=' ')
        print('')


def proverka_koordin(osnov_arg):
    """
    Принимает координаты от пользователя,
    проверяет их на верность установленной формы,
    и отдает два возможных варианта,
    координаты или 'exit'
    """
    while True:
        vvod = input('Введите координаты, формата "строка.столбец"(B.3): ')
        if vvod == 'exit':
            x, point, y = vvod, '', ''
            break
        elif '.' in vvod:
            x, point, y = vvod[0], vvod[1], vvod[2:]# Через срез, для проверки на второй символ точку
            # x = ord(x.upper())# Преобразования буквы в номер ASCII
            if x.isalpha() and y.isnumeric() :
                x = ord(x.upper())# Преобразования буквы в номер ASCII
                if (65 <= int(x) < 65 + osnov_arg) and \
                    point == '.' and \
                    (1 <= int(y) <= osnov_arg):
                # Находится ли в диапазоне по букве, есть ли точка, 
                # Находится ли в диапазоне по числу
                    break
            else:
                print('Форма записи не верна, повторите попытку')
                continue
        else:# ВОзможно этот хвост переписать
            print('Форма записи не верна, повторите попытку')
            continue
    return x, point, y


def add_koordin_to_win(spisok_koordinat, vvod):
    # print(spisok_koordinat)
    if vvod in spisok_koordinat:
        return spisok_koordinat
    else:
        spisok_koordinat.append(vvod)
        return spisok_koordinat


def pod_proga():# Основной код игры
    name = 'Egor'# Покачто статичное имя
    osnov_arg = vvod_ploshadi()
    st_gm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if osnov_arg == 'exit':
        return 'Спасибо что запустили игру.'
    else:
        osnov_arg = int(osnov_arg)# Сразу меняем на число, т.к. потом только числом нужен данный аргумент
        con_bomb = construct_bombs(osnov_arg)
        con_field = construct_field(osnov_arg)
        spisok_koordinat = []# Записываем уникальные верные координаты, 
        # если длина равна (длине поля минус основной аргумент), то выиграли
        print('Приступаем!!!')
        while True:# Слушаем на получение координат
            vivod_poly(con_field)
            vvod = proverka_koordin(osnov_arg)
            spisok_koordinat = add_koordin_to_win(spisok_koordinat, vvod)
            if vvod[0] == 'exit':
                return print('Ну и уходи, а поле в минах осталось.')
            if proverka(vvod[0], vvod[2], osnov_arg, con_bomb) == False:
                sp_gm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return [name, con_bomb, st_gm, sp_gm, False]
            else:
                if len(spisok_koordinat) == len(con_bomb) - osnov_arg:
                    sp_gm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    return [name, con_bomb, st_gm, sp_gm, True]
                podskazka(vvod[0], vvod[2], con_bomb, con_field)


def proga():
    result = pod_proga()
    if result[4] == '1':
        print('You win !!!')
    else:
        print('You Lose !!!')
    conn_db(result)# Записываем в БД результат

if __name__ == '__main__':
    proga()