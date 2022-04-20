"""
Файл где пишется обновленные методы.
"""

#from soupsieve import match


class test:
    '''Данный отрезок кода преобразование в словарь так же надо поместить основной код'''
    osnov_arg = 6
    col_alpha = []
    for i in range(osnov_arg):
        col_alpha.append([chr(65 + i), i + 1])
    col_alpha = dict(col_alpha)
    def proverka_koordin_v2(self):
        ''' Проверка координат готова, но она написана для класса, 
        и принимает словарь, нужно сначало переписать на класс основаной код,
        а после интегрировать преобразование в словарь и данный код
        '''
        # print(self.col_alpha)
        di_alpha = self.col_alpha
        while True:
            try:
                vvod = input('Введите координаты, формата "строка.столбец"(B3): ')
                match vvod:
                    case 'exit':
                        return False
                    case _:
                        alpha, numbr = vvod[0].upper(), int(vvod[1:])# Преобразование для сравнения со словарем
                        if (alpha in di_alpha.keys()) and (numbr in di_alpha.values()):
                            return alpha, '.', numbr
                        else:
                            raise ValueError# т.к. невернаяформа записи, можно и KeyError
            except:
                print('неверная форма записи')

# osnov_arg = 6
# col_alpha = []
# for i in range(osnov_arg):
#     col_alpha.append([chr(65 + i), i + 1])
# col_alpha = dict(col_alpha)
a = test()
q, w, e = a.proverka_koordin_v2()
print(q, w, e)