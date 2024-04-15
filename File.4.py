# import sys
#
#
# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name.lower()
#         self.weight = weight
#         self.price = price
#
#     def __hash__(self):
#         return hash((self.name, self.weight, self.price))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#
#
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['Системный блок: 1500 75890.56',
#           'Монитор Samsung: 2000 34000',
#           'Клавиатура: 200.44 545',
#           'Монитор Samsung: 2000 34000']
#
# d = {}
#
# for i in lst_in:
#     indx = i.index(':')
#     obj = ShopItem(*([i[:indx]] + i[indx+2:].split()))
#     if obj not in d:
#         d[obj] = [obj, 1]
#     else:
#         d[obj][1] += 1

# lst = ['a', 'b', 'a', 'c', 'd']
#
# d = {}
# for i in lst:
#     d.setdefault(i, [i, 0])[1] += 1
#
#
# print(d)

# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name.lower()
#         self.weight = weight
#         self.price = price
#
#     def __hash__(self):
#         return hash((self.name, self.weight, self.price))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#     def __repr__(self):
#         return self.name
#
#
# lst_in = ['Системный блок: 1500 75890.56',
#           'Монитор Samsung: 2000 34000',
#           'Клавиатура: 200.44 545',
#           'Монитор Samsung: 2000 34000']
#
# shop_items = dict()
# for line in lst_in:
#     name, info = line.split(': ')
#     item = ShopItem(name, *map(float, info.split()))
#     shop_items.setdefault(item, [item, 1])[1] += 1
#
#
# print(shop_items)


# class DataBase:
#     def __init__(self, path):
#         self.path = path
#         self.dict_db = {}
#
#     def write(self, record):
#         self.dict_db.setdefault(record, []).append(record)
#
#     def read(self, pk):
#         for value in self.dict_db.values():
#             for obj_rec in value:
#                 if obj_rec.pk == pk:
#                     return obj_rec
#
#
# class Record:
#     PK = 1
#
#     def __init__(self, fio, descr, old):
#         self.pk = self.__class__.PK
#         self.fio = fio
#         self.descr = descr
#         self.old = int(old)
#         self.__class__.PK += 1
#
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#
# lst_in = ['Балакирев С.М.; программист; 33',
#           'Кузнецов Н.И.; разведчик-нелегал; 35',
#           'Суворов А.В.; полководец; 42',
#           'Иванов И.И.; фигурант всех подобных списков; 26',
#           'Балакирев С.М.; преподаватель; 33'
#           ]
#
# db = DataBase('C/')
#
# res = [db.write(Record(*i.split("; "))) for i in lst_in]

import sys


# class BookStudy:
#     def __init__(self, name, author, year):
#         self.name = name.lower()
#         self.author = author.lower()
#         self.year = year
#
#     def __hash__(self):
#         return hash((self.name, self.author))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# lst_in = [
#     'Python; Балакирев С.М.; 2020',
#     'Python ООП; Балакирев С.М.; 2021',
#     'Python ООП; Балакирев С.М.; 2022',
#     'Python; Балакирев С.М.; 2021',
# ]
# lst_bs = [BookStudy(*i.split("; ")) for i in lst_in]
#
# unique_books = len(set(lst_bs))
# print(unique_books)
#
# [print(hash(i)) for i in lst_bs]


# class Dimensions:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
#
#     def __setattr__(self, key, value):
#         if value <= 0:
#             raise ValueError("габаритные размеры должны быть положительными числами")
#         return super().__setattr__(key, value)
#
#
# lst = list(map(lambda x: Dimensions(*map(float, x.split())), input().split("; ")))
# lst.sort(key=hash)
# [print(i.__dict__) for i in lst]


# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = f'_{owner.__name__}__{name}'
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name, None)
#
#     def __set__(self, instance, value):
#         if type(value) not in (int, float) and value <= 0:
#             raise ValueError("с указанными длинами нельзя образовать треугольник")
#         setattr(instance, self.name, value)
#
#
# class Triangle:
#     a = Descriptor()
#     b = Descriptor()
#     c = Descriptor()
#
#     def __init__(self, a, b, c):
#         self.check(a, b, c)
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __len__(self):
#         return int(self.a + self.b + self.c)
#
#     def __call__(self, *args, **kwargs):
#         p = (self.a + self.b + self.c) / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
#     def __setattr__(self, key, value):
#         if key == 'a':
#             self.check(value, self.b, self.c)
#         elif key == 'b':
#             self.check(self.a, value, self.c)
#         elif key == 'c':
#             self.check(self.a, self.b, value)
#         super().__setattr__(key, value)
#
#     @staticmethod
#     def check(a1, b1, c1):
#         if a1 and b1 and c1:
#             a, b, c = sorted([a1, b1, c1])
#             if not c < a + b:
#                 raise ValueError("с указанными длинами нельзя образовать треугольник")
#
#
# tr = Triangle(3.4, 4, 5)
# print(len(tr))
# print(tr())


# lst_in = ['Балакирев; 34; 2048',
#           'Mediel; 27; 0',
#           'Влад; 18; 9012',
#           'Nina P; 33; 0']
#
#
# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = old
#         self.score = score
#
#     def __bool__(self):
#         return bool(self.score)
#
#
# players_filtered = filter(lambda x: bool(x), [Player(*player.split('; ')) for player in lst_in])


# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
#
#     def receive(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         self.inbox_list = [MailItem(*mail.split('; ')) for mail in lst_in]
#
#
# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False
#
#     def set_read(self, fl_read):
#         self.is_read = fl_read
#
#     def __bool__(self):
#         return self.is_read
#
#
# mail = MailBox()
# mail.receive()
# mail.inbox_list[0].set_read(True)
# mail.inbox_list[-1].set_read(True)
# inbox_list_filtered = list(filter(bool, mail.inbox_list))


# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
#
#     def __len__(self):
#         return int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)

# class Ellipse:
#     def __init__(self, *args):
#         if args and len(args) == 4:
#             self.x1, self.x2, self.y1, self.y2 = args
#
#     def __bool__(self):
#         return bool(self.__dict__)
#
#     def get_coords(self):
#         if bool(self):
#             return (self.x1, self.y1), (self.x2, self.y2)
#         raise AttributeError('нет координат для извлечения')
#
#
# lst_geom = [Ellipse() for _ in range(2)]
# lst_geom += [Ellipse(1,2,3,4) for _ in range(2)]
# [print(el.get_coords()) for el in lst_geom if bool(el)]


# from random import randint
#
#
# class Cell:
#     def __init__(self):
#         self.__is_mine = False
#         self.__number = 0
#         self.__is_open = True # False штобы все закрыть
#
#     @property
#     def is_mine(self):
#         return self.__is_mine
#
#     @is_mine.setter
#     def is_mine(self, is_mine):
#         if type(is_mine) is not bool:
#             raise ValueError("недопустимое значение атрибута")
#         self.__is_mine = is_mine
#
#
#     @property
#     def number(self):
#         return self.__number
#
#     @number.setter
#     def number(self, number):
#         if type(number) is not int or number < 0 or number > 8:
#             raise ValueError("недопустимое значение атрибута")
#         self.__number = number
#
#     @property
#     def is_open(self):
#         return self.__is_open
#
#     @is_open.setter
#     def is_open(self, is_open):
#         if type(is_open) is not bool:
#             raise ValueError("недопустимое значение атрибута")
#         self.__is_open = is_open
#
#     def __bool__(self):
#         return not self.__is_open
#
#
# class GamePole:
#     obj = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.obj is None:
#             cls.obj = super().__new__(cls)
#         return cls.obj
#
#     def __init__(self, N, M, total_mines):
#         self.N = N
#         self.M = M
#         self.total_mines = total_mines
#         self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
#
#     @property
#     def pole(self):
#         return self.__pole_cells
#
#     # def add_zero(self): # нужен только для Вариянта 1
#     #     self.pole.insert(0, [Cell() for _ in range(self.M)])
#     #     self.pole.append([Cell() for _ in range(self.M)])
#     #     for row in self.pole:
#     #         row.insert(0, Cell())
#     #         row.append(Cell())
#
#     # def del_zero(self): # нужен только для Вариянта 1
#     #     del self.pole[0]
#     #     del self.pole[-1]
#     #     for i in self.pole:
#     #         del i[0]
#     #         del i[-1]
#
#     def init_pole(self):
#         mines = 0
#         while mines < self.total_mines:
#             cell = self.pole[randint(0, self.N-1)][randint(0, self.M-1)]
#             if not cell.is_mine:
#                 cell.is_mine = True
#                 mines += 1
#
#         ## Вариант 1
#         # self.add_zero()
#         # for i in range(1, self.N+1):
#         #     for j in range(1, self.M+1):
#         #         if not self.pole[i][j].is_mine:
#         #             self.pole[i][j].number = self.func(i, j)
#         # self.del_zero()
#
#         ## Вариант 2
#         indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
#         for x in range(self.N):
#             for y in range(self.M):
#                 if not self.pole[x][y].is_mine:
#                     mines = sum([self.pole[x+i][y+j].is_mine for i, j in indx if 0 <= x+i < self.N and 0 <= y+j < self.M])
#                     self.pole[x][y].number = mines
#
#
#
#     # def func(self, row, col): # нужен только для Вариянта 1
#     #     row1 = self.pole[row-1][col-1].is_mine + self.pole[row-1][col].is_mine + self.pole[row-1][col+1].is_mine
#     #     row2 = self.pole[row][col-1].is_mine + self.pole[row][col+1].is_mine
#     #     row3 = self.pole[row+1][col-1].is_mine + self.pole[row+1][col].is_mine + self.pole[row+1][col+1].is_mine
#     #     return row1 + row2 + row3
#
#     def open_cell(self, i, j):
#         if type(i) is int and i < self.N and type(j) is int and j < self.M:
#             self.pole[i][j].is_open = True
#         else:
#             raise IndexError('некорректные индексы i, j клетки игрового поля')
#
#     def show_pole(self):
#         for row in self.pole:
#             print(*map(lambda x: '#' if x else x.number if not x.is_mine else '*', row))
#
#
# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()

# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
#
#
# if pole.pole[1][2]:
#     pole.open_cell(1, 2)

# pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()
# [print(i) for i in pole.pole]

# class Vector:
#     def __init__(self, *args):
#         self.vectors = args
#
#     @staticmethod
#     def check(v1, v2):
#         if len(v1.vectors) != len(v2.vectors):
#             raise ArithmeticError('размерности векторов не совпадают')
#
#     def __add__(self, other):
#         if type(other) is Vector:
#             self.check(self, other)
#             return Vector(*map(lambda x, y: x + y, self.vectors, other.vectors))
#         elif type(other) in (int, float):
#             return Vector(*map(lambda x: x + other, self.vectors))
#
#     def __iadd__(self, other):
#         if type(other) is Vector:
#             self.check(self, other)
#             self.vectors = tuple(map(lambda x, y: x + y, self.vectors, other.vectors))
#         elif type(other) in (int, float):
#             self.vectors = tuple(map(lambda x: x + other, self.vectors))
#         return self
#
#     def __sub__(self, other):
#         if type(other) is Vector:
#             self.check(self, other)
#             return Vector(*map(lambda x, y: x - y, self.vectors, other.vectors))
#         elif type(other) in (int, float):
#             return Vector(*map(lambda x: x - other, self.vectors))
#
#     def __isub__(self, other):
#         if type(other) is Vector:
#             self.check(self, other)
#             self.vectors = tuple(map(lambda x, y: x - y, self.vectors, other.vectors))
#         elif type(other) in (int, float):
#             self.vectors = tuple(map(lambda x: x - other, self.vectors))
#         return self
#
#     def __mul__(self, other):
#         if type(other) is Vector:
#             self.check(self, other)
#             return Vector(*map(lambda x, y: x * y, self.vectors, other.vectors))
#         elif type(other) in (int, float):
#             return Vector(*map(lambda x: x * other, self.vectors))
#
#     def __imul__(self, other):
#         if type(other) is Vector:
#             self.check(self, other)
#             self.vectors = tuple(map(lambda x, y: x * y, self.vectors, other.vectors))
#         elif type(other) in (int, float):
#             self.vectors = tuple(map(lambda x: x * other, self.vectors))
#         return self
#
#     def __eq__(self, other):
#         self.check(self, other)
#         return all(list(map(lambda x, y: x == y, self.vectors, other.vectors)))

# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __getitem__(self, item):
#         if type(item) is not int or item < 0 or item >= len(self.__dict__):
#             raise IndexError('неверный индекс поля')
#         d = {indx: val for indx, val in enumerate(self.__dict__.values())}
#         return d[item]
#
#     def __setitem__(self, key, value):
#         if type(key) is not int or key < 0 or key >= len(self.__dict__):
#             raise IndexError('неверный индекс поля')
#         d = {indx: key for indx, key in enumerate(self.__dict__.keys())}
#         self.__dict__[d[key]] = value


# r = Record(pk=1, title='Python ООП', author='Балакирев')
# r[0] = 2 # доступ к полю pk
# print(r[0])
# r[1] = 'Супер курс по ООП' # доступ к полю title
# r[2] = 'Балакирев С.М.' # доступ к полю author
# print(r[1]) # Супер курс по ООП
# # r[3] # генерируется исключение IndexError

# class Track:
#     def __init__(self, start_x, start_y):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.points = []
#
#     def add_point(self, x, y, speed):
#         self.points.append([(x, y), speed])
#
#     def check(self, indx):
#         if type(indx) is not int or indx < 0 or indx > len(self.points) - 1:
#             raise IndexError('некорректный индекс')
#
#     def __getitem__(self, item):
#         self.check(item)
#         return self.points[item]
#
#     def __setitem__(self, key, value):
#         self.check(key)
#         self.points[key][1] = value
#
# tr = Track(10, -5.4)
# tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
# tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
# tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
#
# tr[2] = 60
# c, s = tr[2]
# print(c, s)
# res = tr[3] # IndexError


# class Integer:
#     def __init__(self, start_value):
#         self.__start_value = start_value
#
#     @property
#     def start_value(self):
#         return self.__start_value
#
#     @start_value.setter
#     def start_value(self, value):
#         if type(value) is not int:
#             raise ValueError('должно быть целое число')
#         self.__start_value = value
#
#
# class Array:
#     def __init__(self, max_length, cell=Integer):
#         self.max_length = max_length
#         self.cell_class = cell
#         self.arr = [cell(0) for _ in range(self.max_length)]
#
#     def __str__(self):
#         return ' '.join([str(i.start_value) for i in self.arr])
#
#     def __getitem__(self, item):
#         self.validate(item)
#         return self.arr[item].start_value
#
#     def __setitem__(self, key, value):
#         self.validate(key)
#         self.arr[key].start_value = value
#
#     def validate(self, indx):
#         if type(indx) is not int or indx < 0 or indx >= self.max_length:
#             raise IndexError('неверный индекс для доступа к элементам массива')
#
#
# ar_int = Array(10, cell=Integer)
# print(ar_int[3])
# print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
# print(ar_int)
# # ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# # print(ar_int)
# ar_int[10] = 1 # должно генерироваться исключение IndexError

# class IntegerValue:
#     def __set_name__(self, owner, name):
#         self.name = f'_{name}'
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if type(value) is not int:
#             raise ValueError('возможны только целочисленные значения')
#         setattr(instance, self.name, value)
#
#
# class CellInteger:
#     value = IntegerValue()
#
#     def __init__(self, start_value=0):
#         self.value = start_value
#
#
# class TableValues:
#     def __init__(self, rows, cols, cell=None):
#         self.rows = rows
#         self.cols = cols
#         if not cell:
#             raise ValueError('параметр cell не указан')
#         self.cell = cell
#         self.cells = tuple(tuple(cell() for _ in range(self.cols)) for _ in range(self.rows))
#
#     def __getitem__(self, item):
#         row = item[0]
#         col = item[1]
#         return self.cells[row][col].value
#
#     def __setitem__(self, key, value):
#         row = key[0]
#         col = key[1]
#         self.cells[row][col].value = value
#
#
# table = TableValues(2, 3, cell=CellInteger)
# # print(table[0, 1])
# table[1, 1] = 10
# # table[0, 0] = 1.45 # генерируется исключение ValueError
#
# # вывод таблицы в консоль
# for row in table.cells:
#     for x in row:
#         print(x.value, end=' ')
#     print()

class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__count_objs = 0

    def push(self, obj):
        last = self[self.__count_objs - 1] if self.__count_objs > 0 else None

        if last:
            last.next = obj
        if self.top is None:
            self.top = obj
        self.__count_objs += 1

    def pop(self):
        if self.__count_objs == 0:
            return None

        h = self[self.__count_objs - 2] if self.__count_objs > 1 else self[self.__count_objs - 1]
        last = self[self.__count_objs - 1]

        if self.__count_objs == 1:
            self.top = None

        else:
            self[self.__count_objs - 2].next = None

        self.__count_objs -= 1
        return last

    def __check_index(self, item):
        if type(item) is not int or not (0 <= item < self.__count_objs):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        count = 0
        h = self.top
        while h and count < item:
            h = h.next
            count += 1
        return h

    def __setitem__(self, key, value):
        self.__check_index(key)

        obj = self[key]
        prev = self[key - 1] if key > 0 else None

        value.next = obj.next
        if prev:
            prev.next = value


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3

print(st[1].data) # new obj2
# res = st[3] # исключение IndexError

# print(st.top.data)
# i = st.top
# while True:
#     print(i.data, i.next, sep=' /// ')
#     if i.next:
#         i = i.next
#     else:
#  hhjhjhjhjhjhjhj!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###26773684733453454