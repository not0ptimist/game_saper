"""
Файл где присутствует ошибка.
"""
import datetime
import sys
import numpy as np

sys.path.insert(0, '/home/zoljin/work_dir/my_work_1/game_saper')

from lib.circle_find import circle_find
from lib.add_podsk import add_podsk, kostil
# from lib.connect_db import conn_db


class test:

    def construct_bombs_v2(self, bomb):
        '''Создание строки со случайными единицами/минами.
        Нужно придумать рандомайзер на встроенных библиотеках'''
        all_field = bomb ** 2# Длина поля
        zeros = np.zeros((all_field), dtype=np.int32)
        zeros[:bomb] = 1# Заполняем первую "строчку", мнимого квадратного поля
        np.random.shuffle(zeros)
        zeros = zeros.tolist()# При добавлении в базу ругается на тип np.ndarray
        # print(zeros)# Указан для лучшего тестирования, в продакшене убрать
        return zeros


    def construct_field_v2(self, osnov_arg):
        '''Проектирует отображаемое поле'''
        col_alpha = []
        zero_stroki = [0 for i in range(osnov_arg)]# НЕ ЗАБУТЬ! 
        #Ты создал место под список, и используя в разных местах ты по факту используешь одно место
        #и меняется отображение во всех функциях где ссылается на данную участок памяти.
        # используй создание новых адресов памяти, spisok = spisok[:]
        for i in range(osnov_arg + 1):
            match i:
                case 0:
                    col_alpha.append([chr(64 + i), [i + 1 for i in range(osnov_arg)]])
                case _:
                    col_alpha.append([chr(64 + i), zero_stroki])# Вот она ошибка трех вечеров
        col_alpha = dict(col_alpha)
        return col_alpha


    def vivod_poly_v2(self, con_bomb):
        '''Выводит текушее поле, со всеми подсказками, ничего не возвращает'''
        for i in con_bomb.keys():
            print(i, end=' ')
            for j in con_bomb[i][:]:
                print(j, end=' ')
            print('')


    def vvod_ploshadi_v2(self):
        '''ошибка при вводе b3'''
        text_vvoda = 'Введите число для расчета площади и кол-ва мин, по умолчанию значение 6: '
        while True:
            osnov_arg = input(f'{text_vvoda}') or '6'
            if osnov_arg == 'exit':
                break
            elif 6 <= int(osnov_arg) < 11:# Проверка на число
                break
            else:
                print('Ввод неверного значения, повторите. Для выхода введите "exit".')
            continue
        return osnov_arg


    def proverka_koordin_v2(self, con_field):
        ''' Проверка координат готова, но она написана для класса, 
        и принимает словарь, нужно сначало переписать на класс основаной код,
        а после интегрировать преобразование в словарь и данный код
        '''

        while True:
            try:
                vvod = input('Введите координаты, формата "строка.столбец"(B3): ')
                match vvod:
                    case 'exit':
                        return False
                    case _:
                        alpha, numbr = vvod[0].upper(), int(vvod[1:])# Преобразование для сравнения со словарем
                        if (alpha in con_field.keys()) and (numbr in con_field['@'][:]):
                            return vvod
                        else:
                            print('Неверная форма записи')
                        #     raise ValueError# т.к. невернаяформа записи, можно и KeyError
            except ValueError:
                print('Неверная форма записи')
    

    def add_koordin_to_win(self, spisok_koordinat, vvod):
        '''Заполнения уникальными координатами, для проверки на пустые значения'''
        # print(spisok_koordinat)
        if vvod in spisok_koordinat:
            return spisok_koordinat
        else:
            spisok_koordinat.append(vvod)
            return spisok_koordinat
    

    def proverka_v2(self, vvod, con_bomb):
        '''Проверка координат на мину, возвращает True, False, как переключатель для действия'''
        a, n = vvod[0], vvod[1:]
        print(vvod, a, n)
        a = int(ord(a.upper()))
        point = ((a - 65) * 6) + (int(n) - 1)
        if con_bomb[point] == '1':
            return False
        else:
            return True


    def podskazka_v2(self, razmer, vvod, bomb, con_field):
        '''Переписать.Прописывает сумму ближайших мин'''
        a, n = vvod[0], vvod[1:]
        a = a.upper()
        n = int(n) - 1
        ai = int(ord(a))
        tochka = ((ai - 65) * razmer) + n
        num_bomb = circle_find(tochka, bomb, razmer)
        print('1', con_field)
        # print(type(num_bomb), type(a), type(n), type(field), type(bomb))
        # print(num_bomb, a, n, con_field[a][n], bomb)
        # con_field = con_field.copy()

        # Написано 4 способа, но все почемуто записывают кол-во ближайших мин, во все строчки, кроме первой
        # Притом что если отдельно запускать как метод или функцию, то все хорошо.
        # Способ 1
        # field[a][n] = num_bomb
        
        # Способ 2
        # # field_s = field.copy()
        # str_n = field[a]
        # str_n[n] = num_bomb
        # field[a] = str_n

        # Способ 3
        # str_n = field[a]
        # str_n[n] = num_bomb
        # upd_str = {a:str_n}
        # # print('1', field_s)
        # field.update(upd_str.items())

        # Способ 4
        f = kostil(con_field, num_bomb, ai, n)

        # Способ 5
        # f = add_podsk(con_field, num_bomb, a, n)

        print('2', f)
        return f


    def pod_proga_v2(self):
        osnov_arg = self.vvod_ploshadi_v2()
        spisok_koordinat = []# Записываем уникальные верные координаты, 
        # если длина равна (длине поля минус основной аргумент), то выиграли
        if osnov_arg == 'exit':
            print('Спасибо что запустили игру.')
            return False
        else:
            osnov_arg = int(osnov_arg)# Сразу меняем на число, т.к. потом только числом нужен данный аргумент
            con_bomb = self.construct_bombs_v2(osnov_arg)
            con_field = self.construct_field_v2(osnov_arg)
            print('0', con_field)
            spisok_koordinat = []
            while True:
                self.vivod_poly_v2(con_field)
                vvod = self.proverka_koordin_v2(con_field)
                spisok_koordinat = self.add_koordin_to_win(spisok_koordinat, vvod)
                if vvod[0] == 'exit':
                    return print('Ну и уходи, а поле в минах осталось.')
                if self.proverka_v2(vvod, con_bomb) == False:
                    return False
                else:
                    if len(spisok_koordinat) == len(con_bomb) - osnov_arg:#Если длины равны, то пустых клеток нет для хода
                        return True
                    print('0', con_field)
                    con_field = self.podskazka_v2(osnov_arg, vvod, con_bomb, con_field)
                    print(con_field)
                
        # return osnov_arg


    def proga(self):
        result = self.pod_proga_v2()
        if result == '6':
            print('You win !!!')
        else:
            print('You Lose !!!')
        # conn_db(result)# Записываем в БД результат

# osnov_arg = 6
# col_alpha = []
# for i in range(osnov_arg):
#     col_alpha.append([chr(65 + i), i + 1])
# col_alpha = dict(col_alpha)
a = test()
q = a.proga()
# print(q)

# q = a.construct_field_v2(6)
# d = {'@': [1, 1, 1, 1, 1, 1], 'A': [0, 0, 0, 0, 0, 0], 'B': [0, 0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0, 0], 'D': [0, 0, 0, 0, 0, 0], 'E': [0, 0, 0, 0, 0, 0], 'F': [0, 0, 0, 0, 0, 0]}
# q = a.vivod_poly_v2(d)
# osnov_arg = 6
# vvod = 'b3'
# con_bomb = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# con_field = {'@': [1, 2, 3, 4, 5, 6], 'A': [0, 0, 0, 0, 0, 0], 'B': [0, 0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0, 0], 'D': [0, 0, 0, 0, 0, 0], 'E': [0, 0, 0, 0, 0, 0], 'F': [0, 0, 0, 0, 0, 0]}
# q = a.podskazka_v2(osnov_arg, vvod, con_bomb, con_field)
print(q)