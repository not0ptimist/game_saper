# Game_saper_v2.0/Игра сапер

Основная работа:
- переписать в класса
- переписать в словарь поля;

Принцип работы, остается прежним:
- ввод числа для размеров поля, для начала 6 - 16;
- формирование рандомно заполненного минного поля:
- заполнить поле крайними полями(A,B,C-Z) и 1-10;
- вывод пустого поля пользователю;
- ввод координаты;
- проверка координаты на попадание:
  - разбивка на индексы;
  - ищем клетку;
  - если мина:
    - БУМ;
    - возврат и запись в базу.
  - нет мины:
    - проверка на подсказку, есть ли вокруг мины;
    - вывод зачения кол-ва мин поблизости;
    - если нет мин вокруг, то проверка по 4 сторонам на пустые клетки для открытия данной области(нулевой).
  - проверка на кол-во не закрытых клеток((6 * 6) = 36 - 6(мин) = 30):
    - если число закрытых клеток больше "6", то выбор следующего хода;
    - если число закрытых клеток равно "6", то WIN, "Победа, остались только мины";
    - если меньше то это ошибка, и такого не должно быть, как и данного пункта тут!!!

### Ошибки:
- при вводе координат, нажатие Enter приводит "IndexError: string index out of range"
- 

# Game_saper_v1.0/Игра сапер

Принцип работы:
- ввод числа для размеров поля, для начала 6 - 20;
- алгоритм рандома заполнения поля:
  - рандом числа;
  - заполнение, раскидывать по листам;
  - вывод или возврат???
- !!!отказался от первичного заполнения!!!алгоритм заполнения клетки подсказки:
  - проход по миному полю/сразу поиск в строчке;
  - запуск алгоритма на указание.
- заполнить поле крайними полями(A,B,C-Z) и 1-24;
- вывод пустого поля пользователю;
- ввод координаты;
- проверка координаты:
  - разбивка на индексы;
  - ищем клетку;
  - если мина:
    - БУМ;
    - перезапуск игры, "Сыграем ещё?".
  - нет мины:
    - проверка на подсказку, есть ли вокруг мины;
    - вывод зачения кол-ва мин поблизости;
    - если нет мин вокруг, то проверка по 4 сторонам на пустые клетки для открытия данной области(нулевой).
  - проверка на кол-во не закрытых клеток((6 * 6) = 36 - 6(мин) = 30):
    - если число закрытых клеток больше "6", то выбор следующего хода;
    - если число закрытых клеток равно "6", то WIN, "Победа, остались только мины";
    - если меньше то это ошибка, и такого не должно быть, как и данного пункта тут!!!

Дополнительные фишки:
- установка флага, что это мина;
- подсчёт очков;
- таблица лидеров;
- самый быстрый;
- ...
