"""Игра сапер, указываем число.
Функции формируют минное поле, и выводят чистое поле.
Вводим координаты, и смотрим результат.
"""
import numpy as np
from circle_find import circle_find


def construct_bombs(bomb):# Конструктор поля с минами
    all_field = bomb ** 2# Длина поля
    zeros = np.zeros((all_field), dtype=np.int32)
    zeros[:bomb] = 1# Заполняем первую "строчку", мнимого квадратного поля
    np.random.shuffle(zeros)
    print(zeros)
    return zeros


def construct_field(razmer):# Конструктор поля отображения игроку
    alpha = [chr(alpha) for alpha in range(65, 89)]# Список алфавита
    spisok = ['0' for x in range(razmer)]# Основное поле
    matrix = [list(alpha[x]) for x in range(razmer)]# Формирование столбца букв, стобец "x"
    for i in range(razmer):
        matrix[i].extend(spisok)# Добавление полей к столбцу
    matrix.insert(0, [str(x) for x in range(razmer + 1)])# Добавление верхней строки цифр, строка "y"
    return matrix


def proverka(x, y, con_bomb):# Проверка координат на мину
    """Проверка на бомбу"""
    tochka = 4 * (x - 65) + (int(y) - 1)
    if con_bomb[tochka] == 1:
        return False
    else:
        return True


def podskazka(x, y, con_bomb, con_field):# Вывод кол-ва мин
    razmer = len(con_field) - 1
    tochka = 4 * (x - 65) + (int(y) - 1)
    x = x - 64
    y = int(y)
    num_bomb = circle_find(tochka, con_bomb, razmer)# Подсчет ближайших мин
    con_field[x][y] = str(num_bomb)# Вписываем в указанную клетку число мин
    return con_field


def proga():# Основной код игры
    osnov_arg = input('Введите число для расчета площади и кол-ва мин: ')
    if osnov_arg.isnumeric():# Проверка на число, нужно расширять
        osnov_arg = int(osnov_arg)# Сразу меняем на число, т.к. потом только числом нужен данный аргумент
        con_bomb = construct_bombs(osnov_arg)
        con_field = construct_field(osnov_arg)
        print('Приступаем!!!')
        while True:# Слушаем на получение координат
            for i in con_field:# Вывод текущего поля
                for j in i:
                    print(j, end=' ')
                print('')
            vvod = input('Введите координаты, формата "строка.столбец"(B.3): ')
            if vvod == 'exit':
                return print('Ну и уходи.')
            elif '.' in vvod:
                x, point, y = vvod[0], vvod[1], vvod[2:]# Через срез, для проверки на второй символ точку
                x = ord(x.upper())# Преобразования буквы в номер ASCII
                if x >= 65 and x < 65 + osnov_arg and point == '.':
                    if proverka(x, y, con_bomb) == False:
                        return print('BOOM!!!')
                    else:
                        podskazka(x, y, con_bomb, con_field)
            else:
                print('Форма записи не верна, повторите попытку')
    else:
        print('Фуууу, слабак')


if __name__ == '__main__':
    proga()