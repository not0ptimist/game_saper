"""Создал доп файл для теста метода, но он тут работает"""
from lib.circle_find import circle_find

class Test:
    def podskazka_v2(self, vvod, con_bomb, con_field):
        '''Переписать.Прописывает сумму ближайших мин'''
        razmer = len(con_field['E'])
        a, n = vvod[0], vvod[1:]
        a = a.upper()
        n = int(n) - 1
        ai = int(ord(a))
        tochka = ((ai - 65) * 6) + n
        num_bomb = circle_find(tochka, con_bomb, razmer)
        print(type(num_bomb), type(a), type(n), type(con_field), type(con_bomb))
        print(num_bomb, a, n, con_field[a][n], con_bomb)
        # con_field[a][n] = num_bomb

        str_n = con_field[a]
        str_n[n] = num_bomb
        # con_field[a] = str_n

        up_str = {a:str_n}
        print(up_str)
        con_field.update(up_str.items())

        print(con_field)
        return con_field
    
    def vizov(self, vvod, con_bomb, con_field):
        return (self.podskazka_v2(vvod, con_bomb, con_field))

a = Test()
vvod = 'b3'
con_bomb = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
con_field = {'@': [1, 2, 3, 4, 5, 6], 'A': [0, 0, 0, 0, 0, 0], 'B': [0, 0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0, 0], 'D': [0, 0, 0, 0, 0, 0], 'E': [0, 0, 0, 0, 0, 0], 'F': [0, 0, 0, 0, 0, 0]}
q = a.vizov(vvod, con_bomb, con_field)
print(q)