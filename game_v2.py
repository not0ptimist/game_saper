"""
Файл где пишется обновленные методы.
"""
import datetime
import numpy as np

from lib.circle_find import circle_find
# from lib.add_podsk import add_podsk, kostil
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
        print(zeros)# Указан для лучшего тестирования, в продакшене убрать
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
                    col_alpha.append([chr(64 + i), zero_stroki[:]])# Вот она ошибка трех вечеров
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
        ''' Проверка координат готова, 
        через словарь 
        '''
        while True:
            try:
                vvod = input('Введите координаты, формата "строка.столбец"(B3): ')
                if vvod == 'exit':
                    return vvod
                else:
                    alpha, numbr = vvod[0].upper(), int(vvod[1:])# Преобразование для сравнения со словарем
                    if (alpha in con_field.keys()) and (numbr in con_field['@'][:]):
                        return vvod
                    else:
                        print('Неверная форма записи')
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
        '''Проверка координат на мину, 
        возвращает True, False, как переключатель для действия
        '''
        a, n = vvod[0], vvod[1:]
        a = int(ord(a.upper()))
        point = ((a - 65) * 6) + (int(n) - 1)
        print(point, con_bomb[point])
        if con_bomb[point] == 1:
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
        con_field[a][n] = num_bomb
        return con_field


    def pod_proga_v2(self):
        osnov_arg = self.vvod_ploshadi_v2()
        spisok_koordinat = []# Записываем уникальные верные координаты, 
        # если длина равна (длине поля минус основной аргумент), то выиграли
        if osnov_arg == 'exit':
            print('Спасибо что запустили игру.')
            return exit
        else:
            osnov_arg = int(osnov_arg)# Сразу меняем на число, т.к. потом только числом нужен данный аргумент
            con_bomb = self.construct_bombs_v2(osnov_arg)
            con_field = self.construct_field_v2(osnov_arg)
            spisok_koordinat = []

            while True:
                self.vivod_poly_v2(con_field)# Отображение текущего поля
                vvod = self.proverka_koordin_v2(con_field)
                spisok_koordinat = self.add_koordin_to_win(spisok_koordinat, vvod)
                if vvod == 'exit':
                    print('Ну и уходи, а поле в минах осталось.')
                    return exit
                if self.proverka_v2(vvod, con_bomb) == False:
                    return False
                else:
                    if len(spisok_koordinat) == len(con_bomb) - osnov_arg:#Если длины равны, то пустых клеток нет для хода
                        return True
                    con_field = self.podskazka_v2(osnov_arg, vvod, con_bomb, con_field)


    def proga(self):
        result = self.pod_proga_v2()
        match result:
            case 'exit':
                print('Ну и уходи, а поле в минах осталось.')
            case True:
                print('You win !!!')
            case False:
                print('You Lose !!!')
            case _:
                pass
        # conn_db(result)# Записываем в БД результат


a = test()
q = a.proga()
print(q)