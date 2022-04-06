"""Игра сапер, указываем число.
Функции формируют минное поле, и выводят чистое поле.
Вводим координаты, и смотрим результат.
"""
import numpy as np


def construct_bombs(bomb):#конструктор поля с минами
    all_field = bomb ** 2
    zeros = np.zeros((all_field), dtype=np.int32)
    zeros[:bomb] = 1
    np.random.shuffle(zeros)
    zeros = zeros.reshape((bomb, bomb))
    return zeros


def construct_field(razmer):#конструктор поля с именами осей, для отображения
    """Переделать на обычные вложенные списки, через insert добавить буквы
    отображение сделать можно через цельную строку.
    Проблема Numpy, это то что он с цифрами заточен работать, а не с буквами.
    """
    razmer_plus = razmer + 1
    razmer_field = (razmer_plus) ** 2
    zeros = np.zeros((razmer_field), dtype=np.int32)
    zeros.resize((razmer_plus, razmer_plus))
    dt = np.dtype([('name', np.unicode_, 2)])
    zeros_str = np.array(zeros, dtype=dt)
    for i in range(razmer_plus):
        alpha = [chr(alpha) for alpha in range(65, 89)]
        if i == 0:
            zeros_str[0] = [x for x in range(razmer_plus)]
        else:
            zeros_str[i][0] = alpha[i - 1]
    return zeros_str


def proverka(x, y, con_bomb, con_field):#проверка координат на мину
    """Пере"""
    i = 0
    # for stroka in con_field:
        # print(np.where((x)))
        # print(stroka)
        # if stroka.where(x):
        #     print(stroka)
    # x = con_field.where(x) 
    print(x, y, '!!!')
    # y = y - 1
    # if con_bomb[x][y] == '1':
    #     print('popal')
    # else:
    #     print('live')
    pass


def proga():#набросок
    osnov_arg = input('Введите число для расчета площади и кол-ва мин: ')
    if osnov_arg.isnumeric():#проверка
        osnov_arg = int(osnov_arg)#сразу меняем на число, т.к. потом только числом нужен данный аргумент
        con_bomb = construct_bombs(osnov_arg)
        con_field = construct_field(osnov_arg)
        print('cool')
        while True:#слушаем на получение координат
            print(con_field)
            vvod = input('Введите координаты, формата "строка.столбец"(B.3): ')
            if vvod == 'exit':
                return print('Ну и уходи.')
            x, y = vvod.split('.')
            proverka(x, y, con_bomb, con_field)

    else:
        print('foooo')

# construct_field(osnov_arg)
# construct_field(7)

if __name__ == '__main__':
    proga()