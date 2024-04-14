# t = ": ;.,_"
#
# s = 'Python - это круто!'
#
# for i in t:
#     if i in s:
#         s = s.replace(i, '-')
#
# print(s)

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# s = 'Python - это круто!'
# def translate(string):
#     new_str = ''
#     for i in string.lower():
#         if i in t:
#             new_str += t[i]
#         else:
#             new_str += i
#     for j in ":;., ":
#         if j in new_str:
#             new_str = new_str.replace(j, '-')
#     return new_str

# print(translate(s))

# def get_string(s):
#     return ''.join([t[i] if i in t else i for i in s.lower()])
# print(get_string(s))

# import time
# def decor_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         stop = time.time()
#
#         print(f'Время выполнения функции "{res[1]}": {stop-start} сек.')
#         return
#     return wrapper
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# s = 'Python - это круто!'
#
# @decor_time
# def translate(string):
#     new_str = ''
#     for i in string.lower():
#         if i in t:
#             new_str += t[i]
#         else:
#             new_str += i
#     for j in ":;., ":
#         if j in new_str:
#             new_str = new_str.replace(j, '-')
#     return new_str, 'translate'
#
# translate(s)


# lst = list(range(100))
# print(lst)

# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# n = len(cities)
# gen = (cities[i % n] for i in range(1000000))
#
# print(*(next(gen) for i in range(20)))

# print([i for i in range(1_0)])

# N = 7
#
# # put your python code here
# def func():
#     a, b, c = 1, 1, 1
#     while True:
#         yield a
#         a, b, c, = b, c, a + b + c
#
# x = func()
# for i in range(N):
#     print(next(x), end=' ')

#
# import random
# from string import ascii_lowercase, ascii_uppercase
#
# # установка зерна датчика случайных чисел (не менять)
# random.seed(1)
#
# # здесь продолжайте программу
#
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# N = 10
# l = len(chars)
#
#
# def func(n):
#
#     pas = ''
#     while n > 0:
#         indx = random.randint(0, l)
#         pas += chars[indx]
#         n -= 1
#     yield pas
#
# for i in range(5):
#     print(next(func(N)))

# import random
# from string import ascii_lowercase, ascii_uppercase
#
# # установка зерна датчика случайных чисел (не менять)
# random.seed(1)
#
# # здесь продолжайте программу
#
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# N = 10
# l = len(chars)
# def func(n):
#     while True:
#         pas = ''
#         for i in range(n):
#             indx = random.randint(0, l)
#             pas += chars[indx]
#         yield pas
#
# x = func(N)
# for i in range(5):
#     print(next(x))


# put your python code here


# x = map(int, ['1', '2', '3'])
# print(next(x))

# import random
#
# # Установка начального значения (зерна)
# random.seed(42)
#
# # Генерация случайного числа
# for _ in range(5):
#
#     print(random.randint(1, 100))

# x = input().split()
# x1 = input().split()
#
# res = list(map(lambda x, y: (int(x), int(y)), x, x1))
# print(res)

# x = '12345'
# y = '23456'
#
# r = [x, y]
#
# print(*r)
#
#
# print(*zip(*r))

# f = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'
# a = f.split()
# it=iter(a)
# z=list(zip(it,it,it))
# for i in z:
#     print(*i)

# s = input()
#
# # здесь продолжайте программу
# lst = list(zip(s, range(10)))
# print(lst)

# ввод строки в переменную s (переменную в программе не менять)
# s = input()
#
# # здесь продолжайте писать программу
# lst = list(map(int, s.split()))
# lst.sort()
# tp_lst = sorted(tuple(map(int, s.split())))
#
#
#
# print(lst)
# print(tp_lst)

# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
#
# def get_sort(d):
#     return [v for k, v in sorted(d.items(), reverse=True)]
#
# print(get_sort(d))

# x = input().split()
# l = ['до', 'ре', 'ми', 'фа', 'соль', 'л', 'си']
# d = dict(zip(range(7), l))
# d_res = {}
# for i in x:
#
#     for k, v in d.items():
#         if i == v:
#             d_res[k] = d[k]
# print(d_res)

# a = 5
#
#
# print(bin(a))
# # print(bin(6))
# a = ~a
# print(bin(a))

# print(bin(106))
# print(0b00001001)

# x = 6
# if x % 2 == 0 or x % 3 == 0:
#     print('ok')
# else:
#     print('NO')
#
# import random
# # установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
#
# # начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
# N = 10
# P = [[0] * N for i in range(N)]
# count = 0
# while count < 10:
#     i = random.randint(1, 8)
#     j = random.randint(1, 8)
#     s = sum(P[i - 1][j - 1:j + 2]) + sum(P[i][j - 1:j + 2]) + sum(P[i + 1][j - 1:j + 2])
#     if s:
#         continue
#     else:
#         P[i][j] = 1
#         count += 1
#
#
# for i in P:
#     print(*i)


# x = [1,2,3,'ght']
# print(id(x))
# print(id(x[3][1]))
# print(x[3][1])
# bool


# class Goods:
#     """KJGKK"""
#     title = "Мороженое"
#     weight = 154
#     tp = "Еда"
#     price = 1024
#
# g = Goods()
#
# g.tp = 'ghgh'
# print(Goods.tp)
# print(g.tp)


# class Car:
#     ...
#
#
# d = dict(model="Тойота", color="Розовый", number="П111УУ77")
#
# [setattr(Car, *i) for i in d.items()]

# print(Car.__dict__['color'])


# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
# p1 = Person()
# p1.job = 'уборщик'
#
# print('job' in p1.__dict__)


# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         for i in self.data:
#             if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
#                 print(i, end=' ')
#
#
# graph_1 = Graph()
# l = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
# graph_1.set_data(l)
# graph_1.draw()


# программу не менять, только добавить два метода
# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']  # считывание списка строк из входного потока
#
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     # здесь добавлять методы
#     def insert(self, data):
#         for i in data:
#             self.lst_data.append(dict(zip(self.FIELDS, i.split())))
#
#     def select(self, a, b):
#         return self.lst_data[a:] if len(self.lst_data) < b else self.lst_data[a:b+1]
#
#
# db = DataBase()
# db.insert(lst_in)
# print(db.select(0, 1))
# print(lst_in[0:6])


# class Translator:
#     def add(self, eng, rus):
#         if 'tr' not in self.__dict__:
#             self.tr = {}
#
#         self.tr.setdefault(eng, [])
#         # здесь продолжайте метод add
#         if rus not in self.tr[eng]:
#             self.tr[eng] += [rus]
#
#     def remove(self, eng):
#         # здесь продолжайте метод remove
#         del self.tr[eng]
#
#     def translate(self, eng):
#         # здесь продолжайте метод translate
#         return self.tr[eng]
#
#
# # здесь создавайте объект класса Translator
# tr = Translator()
#
#
# tp = (('tree', 'дерево'), ('car', 'машина'), ('car', 'автомобиль'), ('leaf', 'лист'), ('river', 'река'), ('go', 'идти'), ('go', 'ехать'), ('go', 'ходить'), ('milk', 'молоко'))
#
#
# [tr.add(k, v) for k, v in tp]
#
# tr.remove('car')
# print(*tr.translate('go'))


# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = [Point(i, i, 'yellow') if i == 2 else Point(i, i, 'yellow') for i in range(1, 2000, 2)]
# print(points)

# import random
# class Graph:
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
# class Line(Graph):
#     pass
#
# class Rect(Graph):
#     pass
#
# class Ellipse(Graph):
#     pass
#
#
# elements = [random.choice([Line, Rect, Ellipse])(random.randint(1, 101),
#            random.randint(1, 101), random.randint(1, 101), random.randint(1, 101)) for i in range(217)]
#
# # elements = [i if not isinstance(i, Line) else Line(0, 0, 0, 0) for i in elements]
#
# print(elements[3].__class__)
#
# tp = Rect(1,2,3,4)
# print(tp.__class__.__name__)

# здесь объявите класс TriangleChecker
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c
#
#     def is_triangle(self):
#         self.lst = [self.a, self.b, self.c]
#         if any(type(i) not in (int, float) or i <= 0 for i in self.lst):
#             return 1
#
#         elif max(self.lst) >= sum(sorted(self.lst)[:2]):
#             return 2
#         return 3
#
#
# # a, b, c = map(int, input().split())  # эту строчку не менять
# # здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
# a, b, c = 3, 4, 5
#
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())


# здесь объявляются все необходимые классы
# class Graph:
#
#     def __init__(self, data, is_show=True):
#         self.data = data[:]
#         self.is_show = is_show
#
#
#     def check(func):
#         def wrapper(self):
#             if self.is_show:
#                 func(self)
#             else:
#                 print('Отображение данных закрыто')
#         return wrapper
#
#     def set_data(self, data):
#         self.data = data
#
#     @check
#     def show_table(self):
#         print(*self.data)
#
#     @check
#     def show_graph(self):
#         print('Графическое отображение данных:', *self.data)
#
#     @check
#     def show_bar(self):
#         print('Столбчатая диаграмма:', *self.data)
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# # считывание списка из входного потока (эту строку не менять)
# data_graph = list(map(int, input().split()))
#
# # здесь создаются объекты классов и вызываются нужные методы
# gr = Graph(data_graph)
#
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()

# здесь пишите программу
# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu, *mem_slots):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = [*mem_slots] if len(mem_slots) < self.total_mem_slots else [*mem_slots][:4]
#
#     def get_config(self):
#         self.new_list = [f'{i.name} - {i.volume}' for i in self.mem_slots]
#         return [f'Материнская плата: {self.name}',
#                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
#                f'Слотов памяти: {self.total_mem_slots}',
#                f'Память: {"; ".join(self.new_list)}']
#
#
# cpu = CPU('asus', 1333)
# mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
# mb = MotherBoard('Asus', cpu, mem1, mem2)
# print(mb.get_config())

# lst_in = ['1. Первые шаги в ООП',
#           '1.1 Как правильно проходить этот курс',
#           '1.2 Концепция ООП простыми словами',
#           '1.3 Классы и объекты. Атрибуты классов и объектов',
#           '1.4 Методы классов. Параметр self',
#           '1.5 Инициализатор init и финализатор del',
#           '1.6 Магический метод new. Пример паттерна Singleton',
#           '1.7 Методы класса (classmethod) и статические методы (staticmethod)']

# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(1, 2)
#
# print(Point.pt)

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"
#
# obj = AbstractClass()
# print(obj)

# здесь объявляйте класс SingletonFive
# class SingletonFive:
#     lst = []
#
#     def __new__(cls, *args, **kwargs):
#         if len(cls.lst) < 5:
#             cls.lst.append(super().__new__(cls))
#         return cls.lst[-1]
#
#     def __init__(self, name):
#         self.name = name
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять
# for i in objs:
#     print(i)
#

TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#
#         if TYPE_OS == 1:
#             obj = super().__new__(DialogWindows)
#         else:
#             obj = super().__new__(DialogLinux)
#         obj.name = args[0]
#         return obj
# dlg = Dialog('jjbbb')
# print(dlg)

# здесь объявляется класс Point
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self):
#         obj = Point(self.x, self.y)
#         return obj
#
#
# pt = Point(1, 2)
# pt_clone = pt.clone()
#
# print(pt)
# print(pt_clone.x)


# from string import ascii_lowercase, digits
#
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     @classmethod
#     def check_name(cls, name):
#         if 50 < len(name) or len(name) < 3 or not all(i in cls.CHARS_CORRECT for i in name):
#             raise ValueError("некорректное поле name")
#
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     @classmethod
#     def check_name(cls, name):
#         if 50 < len(name) or len(name) < 3 or not all(i in cls.CHARS_CORRECT for i in name):
#             raise ValueError("некорректное поле name")
#
#
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
# print(html)

# from string import ascii_uppercase, digits
#
# class CardCheck:
#
#     CHARS_FOR_NAME = ascii_uppercase + digits
#     @staticmethod
#     def check_card_number(number):
#         number_new = ''
#         for i in number:
#             if i.isdigit():
#                 i = 'x'
#                 number_new += i
#             elif i == '-':
#                 number_new += i
#             else:
#                 number_new += '1'
#         return 'xxxx-xxxx-xxxx-xxxx' == number_new
#
#     @classmethod
#     def check_name(cls, name):
#         return name.count(' ') == 1 and set(name.replace(' ', '')) < set(cls.CHARS_FOR_NAME)
#
# is_number = CardCheck.check_card_number("1214-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# print(is_number)
# print(is_name)

# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f'воспроизведение видео {self.name}')
#
# class YouTube:
#     videos = []
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
#
# v1 = Video()
# v2 = Video()
# v1.create('Python')
# v2.create('Python ООП')
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)

# class AppStore:
#     lst = []
#
#     def add_application(self, app):
#         self.lst.append(app)
#
#     def remove_application(self, app):
#         self.lst.remove(app)
#
#     def block_application(self, app):
#         app.blocked = True
#
#     def total_apps(self):
#         return len(self.lst)
#
# class Application:
#     def __init__(self,name):
#         self.name = name
#         self.blocked = False

# class Viber:
#     d = {}
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.d[id(msg)] = msg
#
#     @classmethod
#     def remove_message(cls, msg):
#         cls.d.pop(id(msg))
#
#     @classmethod
#     def set_like(cls, msg):
#         msg.fl_like = not msg.fl_like
#
#     @classmethod
#     def show_last_message(cls, number):
#         for m in tuple(cls.d)[-number:]:
#             print(m)
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.d)
#
# class Message:
#     def __init__(self, text, fl_like=False):
#         self.text = text
#         self.fl_like = fl_like
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)

# class Clock:
#     def __init__(self):
#         self.__time = 0
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
#     def __check_time(self, tm):
#         return type(tm) == int and 0 <= tm < 100000
#
# clock = Clock()
# clock.set_time(4530)
# print(clock.get_time())

# class Money:
#     def __init__(self, money):
#         if self.__check_money(money):
#             self.__money = money
#         else:
#             self.__money = 0
#
#     @classmethod
#     def __check_money(cls, money):
#         return type(money) == int and money >= 0
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, money):
#         self.__money += money.__money

# class Book:
#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self,):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price

# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.set_coords(x1, y1, x2, y2)
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1, self.__y1 = x1, y1
#         self.__x2, self.__y2 = x2, y2
#
#     def get_coords(self):
#         return (self.__x1, self.__y1 , self.__x2, self.__y2)
#
#     def draw(self):
#         print(*self.get_coords())
#
# line = Line(1, 2, 3, 4)
# res = line.__dict__
# print(res)
# line.draw()

# class Point:
#     def __init__(self, x, y):
#         if self.check(x) and self.check(y):
#             self.__x, self.__y = x, y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     @staticmethod
#     def check(item):
#         return type(item) in (int, float)
#
# class Rectangle:
#     def __init__(self, *args):
#         if len(args) == 4:
#             self.__sp = Point(*args[:2])
#             self.__ep = Point(*args[2:])
#         else:
#             self.set_coords(*args)
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f'Прямоугольник с координатами: {self.__sp.get_coords()}{self.__ep.get_coords()}')
#
# # rect = Rectangle(Point(0, 0), Point(20, 34))
# rect = Rectangle(0, 0, 20, 34)
#
#
# rect.draw()
# res = rect.get_coords()
# print(res)

# class LinkedList:
#     """объявите класс LinkedList, который будет представлять связный список в целом
#     и иметь набор следующих методов:
#     И локальные публичные атрибуты:
#     head - ссылка на первый объект связного списка (если список пустой, то head = None);
#     tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
#     """
#
#     def __init__(self):
#         self.head = self.tail = None
#         self.__data = []
#
#     def update_head_tail(self):
#         if len(self.__data) == 0:
#             self.head = self.tail = None
#         elif len(self.__data) == 1:
#             self.head = self.tail = self.__data[0]
#         else:
#             self.head = self.__data[0]
#             self.tail = self.__data[-1]
#
#     def add_obj(self, obj):
#         """добавление нового объекта obj класса ObjList в конец связного списка;
#         """
#         if self.tail:
#             obj.set_prev(self.tail)
#             self.tail.set_next(obj)
#         self.__data.append(obj)
#         self.update_head_tail()
#
#     def remove_obj(self):
#         """удаление последнего объекта из связного списка;
#         """
#         self.__data.pop()
#         self.update_head_tail()
#         if self.tail:
#             self.tail.set_next(None)
#
#
#
#     def get_data(self):
#         """получение списка из строк локального свойства __data всех объектов связного списка.
#         """
#         return [i.get_data() for i in self.__data]
#
# class ObjList:
#     """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
#     __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
#     __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
#     __data - строка с данными.
#     Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
#     """
#     def __init__(self, data):
#         self.__prev = None
#         self.__data = None
#         self.__next = None
#         self.__data = data
#
#     def set_next(self, obj):
#         """изменение приватного свойства __next на значение obj;
#         """
#         self.__next = obj
#
#     def set_prev(self, obj):
#         """изменение приватного свойства __prev на значение obj;
#         """
#         self.__prev = obj
#
#     def get_next(self):
#         """получение значения приватного свойства __next;
#         """
#         return self.__next
#
#     def get_prev(self):
#         """получение значения приватного свойства __prev;
#         """
#         return self.__prev
#
#     def set_data(self, data):
#         """изменение приватного свойства __data на значение data;
#         """
#         self.__data = data
#
#     def get_data(self):
#         """получение значения приватного свойства __data.
#         """
#         return self.__data
#
#
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# lst.add_obj(ObjList("данные 34"))
#    # ['данные 1', 'данные 2', 'данные 3']

# lst.remove_obj()
# lst.remove_obj()
# lst.remove_obj()
#
# res = lst.get_data()
# print(lst.head.get_next())
# print(lst.head.get_prev())
# print()
# print(res)
# print(lst.__dict__)

# from string import ascii_lowercase, ascii_uppercase, digits
# import random
#
# class EmailValidator:
#     def __new__(cls):
#         pass
#
#     CHECK = ascii_uppercase + ascii_lowercase + digits + '@_.'
#     CHECK1 = ascii_uppercase + ascii_lowercase + digits + '_'
#
#     @classmethod
#     def get_random_email(cls):
#         return ''.join([random.choice(cls.CHECK1) for _ in range(random.randint(1, 100))]) + '@gmail.com'
#
#     @classmethod
#     def check_email(cls, email):
#         fl = False
#         if not cls.__is_email_str(email):
#             return fl
#         if not all(i in cls.CHECK for i in email) or email.count('@') > 1:
#             return fl
#         if len(email[:email.index('@')]) > 100 or len(email[email.index('@')+1:]) > 50 or email[email.index('@')+1:].count('.') < 1:
#             return fl
#         if email.count('..') != 0:
#             return fl
#         return True
#
#     @staticmethod
#     def __is_email_str(email):
#         return type(email) == str
#
# res = EmailValidator.get_random_email()
# print(res)
# print(EmailValidator.check_email(res))

# class Car:
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         self.__model = model

# f = 21.1
# rounded_f = round(f, 1)  # Округляем до одного знака после запятой
# x = str(rounded_f) + '0'
# w = int(x)
# print(w)  # Результат: 211


##### ВАРИАНТ 1
# from random import randint
#
#
# class Cell:
#     def __init__(self, around_mines, mine):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = False
#
#
# class GamePole:
#     def __init__(self, N, M):
#         self.M = M
#         self.N = N
#         self.pole = []
#         for i in range(N):
#             lst_temp = []
#             for j in range(N):
#                 lst_temp.append(Cell(0, 0))
#             self.pole.append(lst_temp)
#
#         self.init()
#
#     def init(self):
#         for m in range(self.M):
#             i = randint(0, self.N - 1)
#             j = randint(0, self.N - 1)
#             if self.pole[i][j] == 1:
#                 continue
#             else:
#                 self.pole[i][j].mine = 1
#
#         for i in self.pole:
#             i.insert(0, Cell(0, 0))
#             i.append(Cell(0, 0))
#         self.pole.insert(0, [Cell(0,0) for i in range(len(self.pole[0]))])
#         self.pole.append([Cell(0, 0) for i in range(len(self.pole[0]))])
#
#         for i in range(1, len(self.pole)-1):
#             for j in range(1, len(self.pole[1])-1):
#                 n1 = self.pole[i-1][j-1].mine + self.pole[i-1][j].mine + self.pole[i-1][j+1].mine
#                 n2 = self.pole[i][j-1].mine + self.pole[i][j+1].mine
#                 n3 = self.pole[i+1][j-1].mine + self.pole[i+1][j].mine + self.pole[i+1][j+1].mine
#                 self.pole[i][j].around_mines = n1 + n2 + n3
#
#         for i in self.pole:
#             i.pop(0)
#             i.pop(-1)
#         self.pole.pop(0)
#         self.pole.pop(-1)
#
#
#     def show(self):
#         for i in self.pole:
#             print(*list(map(lambda x: '#' if x.fl_open else '*' if x.mine == 1 else x.around_mines, i)))
#
#
# pole_game = GamePole(10, 12)
# pole_game.show()


##### ВАРИАНТ 2 (оптимизировал)
# from random import randint
#
#
# class Cell:
#     def __init__(self, around_mines, mine):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = False
#
#
# class GamePole:
#     def __init__(self, N, M):
#         self.M = M
#         self.N = N
#         self.pole = []
#         self.init()  # вызываем метод init()
#
#     def init(self):
#         # Создаём поле из ячеек(объектов класса Cell с нулевыми атрибутами)
#         # и также с дополнительными ячейками(объектами) по периметру,
#         # что бы при подсчете мин вокруг ячейки избежать ошибки IndexError(выход за пределы списка)
#         self.pole = [[Cell(0, 0) for _ in range(self.N + 2)] for _ in range(self.N + 2)]
#
#         # устанавливаем рандомно мины по полю кроме ячеек по периметру
#         for m in range(self.M):
#             i = randint(1, self.N)
#             j = randint(1, self.N)
#             if self.pole[i][j] == 1:  # если мина уже установлена в данной ячейки пропускаем цикл
#                 continue
#             else:
#                 self.pole[i][j].mine = 1
#
#         # Считаем мины вокруг каждой ячейки кроме тех что по периметру
#         # и устанавливаем результат в атрибут 'around_mines'
#         n = len(self.pole) - 1
#         for i in range(1, n):
#             for j in range(1, n):
#                 row_1 = self.pole[i - 1][j - 1].mine + self.pole[i - 1][j].mine + self.pole[i - 1][j + 1].mine
#                 # row_1 = sum(list(map(lambda x: x.mine, self.pole[i-1]))[j-1:j+2]) # можно и со срезами но менее читабельно
#                 row_2 = self.pole[i][j - 1].mine + self.pole[i][j + 1].mine
#                 row_3 = self.pole[i + 1][j - 1].mine + self.pole[i + 1][j].mine + self.pole[i + 1][j + 1].mine
#                 self.pole[i][j].around_mines = row_1 + row_2 + row_3
#
#         # Обрезаем лишние ячейки по периметру поля
#         self.pole = [[self.pole[i][j] for j in range(1, self.N + 1)] for i in range(1, self.N + 1)]
#
#     def show(self):
#         for i in self.pole:
#             print(*list(map(lambda x: '#' if x.fl_open else '*' if x.mine == 1 else x.around_mines, i)))
#
#
# pole_game = GamePole(10, 12)
# pole_game.show()


#### ВАРИАНТ 3
# from random import randint
#
#
# class Cell:
#     def __init__(self, around_mines, mine):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = False
#
#
# class GamePole:
#     def __init__(self, N, M):
#         self.M = M
#         self.N = N
#         self.pole = []
#         self.init()  # вызываем метод init()
#
#     def init(self):
#         # Создаём поле из ячеек(объектов класса Cell с нулевыми атрибутами)
#         # и также с дополнительными ячейками(объектами) по периметру,
#         # что бы при подсчете мин вокруг ячейки избежать ошибки IndexError(выход за пределы списка)
#         self.pole = [[Cell(0, 0) for _ in range(self.N + 2)] for _ in range(self.N + 2)]
#
#         # устанавливаем рандомно мины по полю кроме ячеек по периметру
#         for m in range(self.M):
#             i = randint(1, self.N)
#             j = randint(1, self.N)
#             if self.pole[i][j] == 1:  # если мина уже установлена в данной ячейки пропускаем цикл
#                 continue
#             else:
#                 self.pole[i][j].mine = 1
#
#         # Считаем мины вокруг каждой ячейки кроме тех что по периметру
#         # и устанавливаем результат в атрибут 'around_mines'
#         n = len(self.pole) - 1
#         for x in range(1, n):
#             for y in range(1, n):
#                 count = 0
#                 for i in range(-1, 2):
#                     for j in range(-1, 2):
#                         count += self.pole[x + i][y + j].mine
#                 self.pole[x][y].around_mines = count
#
#         # Обрезаем лишние ячейки по периметру поля
#         self.pole = [[self.pole[i][j] for j in range(1, self.N + 1)] for i in range(1, self.N + 1)]
#
#     def show(self):
#         for i in self.pole:
#             print(*list(map(lambda x: '#' if x.fl_open else '*' if x.mine == 1 else x.around_mines, i)))
#
#
# pole_game = GamePole(10, 12)
# pole_game.show()


# class WindowDlg:
#     def __init__(self, title, width, height):
#         self.__title = title
#         self.__width, self.__height = width, height
#
#     def show(self):
#         print(f"{self.__title}: {self.__width}, {self.__height}")
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         if self.check(width):
#             self.__width = width
#             self.show()
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         if self.check(height):
#             self.__height = height
#             self.show()
#
#     @staticmethod
#     def check(num):
#         return type(num) == int and 0 <= num <= 10_000
#
# j = WindowDlg('HJHJ', 56, 55)
# j.height = 'k'

move_zero1 = [1, 0, 0, 2, 0, 1, 3]


# def move_zeros(lst):
#     n = lst.count(0)
#     for k in range(n):
#         for i in range(len(lst)-1):
#             if lst[i] == 0:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#     return lst
#
#
# print(move_zeros(move_zero1))
#
#
# def move_zeros(array):
#     for i in array:
#         if i == 0:
#             array.remove(i) # Remove the element from the array
#             array.append(i) # Append the element to the end
#     return array
#
# print(move_zeros(move_zero1))

# def move_zeros(lst):
#
#     for i, k in enumerate(lst):
#         if k == 0:
#             a = lst.pop(i)
#             lst.append(a)
#
#     return lst
#
# print(move_zeros(move_zero1))

# def move_zeros(array):
#     return sorted(array, key=lambda x: x==1 and type(x) is not bool, reverse=False)
#
# print(move_zeros(move_zero1))

# pig = ('Hello world !') # igPay atinlay siay oolcay
#
#
# def pig_it(string):
#     return ' '.join(list(map(lambda x: ''.join(sorted(x, key=lambda y: y == x[0])) + 'ay' if x.isalpha() else x, string.split())))


# print(pig_it(pig))

# def pig_it(string):
    # lst = string.split()
    # res = []
    # for i in lst:
    #     if i.isalpha():
    #         res.append(f'{i[1:]}{i[0]}ay')
    #     else:
    #         res.append(i)
    # return ' '.join(res)

# def pig_it(string):
#     return ' '.join([f'{i[1:]}{i[0]}ay' if i.isalpha() else i for i in string.split()])
# print(pig_it(pig))

# def make_readable(seconds):
#     hours, rest = divmod(seconds, 3600)
#     minuts, seconds_ = divmod(rest, 60)
#     return f"{str(hours).rjust(2,'0')}:{str(minuts).rjust(2,'0')}:{str(seconds_).rjust(2,'0')}"
#
# print(make_readable(0))
# def make_readable(seconds):
#     hours, rest = divmod(seconds, 3600)
#     minuts, seconds_ = divmod(rest, 60)
#     return f"{hours:02d}:{minuts:02d}:{seconds_:02d}"
#
# print(make_readable(359999))

# def rgb(r, g, b):
#     return ''.join(map(lambda x: f'0{x}' if len(x) == 1 else x,
#            [f'{hex(i).replace("0x", "").upper()}' if i < 256 else f'{hex(255)[2:].upper()}' for i in (r, g, b)]))
#
# print(rgb(255, 2, 300))
# def rgb(r, g, b):
#     res = []
#     for i in (r, g, b):
#         if i > 255:
#             i = 255
#         elif i < 1:
#             i = 0
#         else:
#             i = i
#         res.append(hex(i).replace("0x", "").upper())
#     return ''.join(list(map(lambda x: f'0{x}' if len(x) == 1 else x, res)))
#
#
# print(rgb(-23, 2, 300))


# def rgb(r, g, b):
#     clip = lambda x: min(255, max(x, 0))
#     return f'{clip(r):02X}{clip(g):02X}{clip(b):02X}'
#
#
# print(rgb(-23, 2, 300))


# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, next_):
#         if type(next_) is StackObj or next_ is None:
#             self.__next = next_
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.last = None
#         self.lst_objects = []
#
#     def push(self, obj):
#         if len(self.lst_objects) == 0:
#             self.top = obj
#         elif len(self.lst_objects) == 1:
#             self.top.next = obj
#             self.last = obj
#         else:
#             self.last.next = obj
#             self.last = obj
#         self.lst_objects.append(obj)
#
#     def pop(self):
#         res = self.lst_objects.pop()
#         if len(self.lst_objects) > 0:
#             self.lst_objects[-1].next = None
#         if len(self.lst_objects) == 1:
#             self.last = None
#         if len(self.lst_objects) == 0:
#             self.top = None
#         return res
#
#
#     def get_data(self):
#         return list(map(lambda x: x.data, self.lst_objects))
#
#
#
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# st.pop()
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
#
# print(st.lst_objects)
# print(list(map(lambda x: x.next, st.lst_objects)))

# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024
#
#     def __init__(self, x=0, y=0):
#         self.__x = self.check(x)
#         self.__y = self.check(y)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.check(value):
#             self.__x = value
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.check(value):
#             self.__y = value
#
#     @classmethod
#     def check(cls, value):
#         return value if type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD else 0
#
#     @staticmethod
#     def norm2(vector):
#         return vector.x * vector.x + vector.y * vector.y
#
# v1 = RadiusVector2D()
# v2 = RadiusVector2D(1)
# v3 = RadiusVector2D(1.5, 1200)
#
#
# print(v1.x, v1.y)
# print(v2.x, v2.y)
# print(v3.x, v3.y)

# from math import sqrt
#
#
# class PathLines:
#     def __init__(self, *args):
#         self.lst_obj = [*args]
#
#     def get_path(self):
#         return self.lst_obj
#
#     def get_length(self):
#         l1 = sqrt((self.lst_obj[0].x - 0) ** 2 + (self.lst_obj[0].y - 0) ** 2)
#         if len(self.lst_obj) < 2:
#             return l1
#         else:
#             res = [l1]
#             for i, v in enumerate(self.lst_obj[1:], 1):
#                 res.append(sqrt((v.x - self.lst_obj[i-1].x) ** 2 + (v.y - self.lst_obj[i-1].y) ** 2))
#             return sum(res)
#
#     def add_line(self, line):
#         self.lst_obj.append(line)
#
#
# class LineTo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# result = list(map(lambda x, y: x + y, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
# print(result)

# from math import sqrt
#
#
# class LineTo:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
# class PathLines:
#     def __init__(self, *args):
#         self.lst_obj = [LineTo()] + list(args)
#
#     def get_path(self):
#         return self.lst_obj[1:]
#
#     def get_length(self):
#         return sum(list(map(lambda l1, l2: sqrt((l2.x-l1.x)**2 + (l2.y - l1.y)**2), self.lst_obj, self.get_path())))
#
#     def add_line(self, line):
#         self.lst_obj.append(line)
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))


# dist = p.get_length()
# print(dist)

# class TreeObj:
#     def __init__(self, indx, value=None):
#         self.indx = indx
#         self.value = value
#         self.__left = None
#         self.__right = None
#
#     @property
#     def left(self):
#         return self.__left
#
#     @left.setter
#     def left(self, left):
#         self.__left = left
#
#     @property
#     def right(self):
#         return self.__right
#
#     @right.setter
#     def right(self, right):
#         self.__right = right
#
#
# class DecisionTree:
#     lst_obj = []
#
#     @classmethod
#     def predict(cls, root, x):
#         res = None
#         indx = 0 # 1
#         for i, v in enumerate(x):
#             if indx == cls.lst_obj[i].indx:
#                 if v:
#                     res = cls.lst_obj[indx].left
#                 else:
#                     res = cls.lst_obj[indx].right
#                 if res.indx < 0:
#                     break
#                 indx = res.indx
#             else:
#                 continue
#         return res.value

#     @classmethod
#     def predict(cls, root, x):
#         for i, v in enumerate(x):
#             if root.indx == i:
#                 if v == 1:
#                     root = root.left
#                 else:
#                     root = root.right
#                 if root.indx < 0:
#                     break
#             else:
#                 continue
#         return root.value
#
#
#     @classmethod
#     def add_obj(cls, obj, node=None, left=True):
#         # cls.lst_obj.append(obj)
#         if node:
#             if left:
#                 node.left = obj
#             else:
#                 node.right = obj
#         return obj
#
#
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
# x = [1, 0, 1]
# res = DecisionTree.predict(root, x) # будет программистом
# print(res)


# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# v_111 = DecisionTree.add_obj(TreeObj(3), v_11)
# v_112 = DecisionTree.add_obj(TreeObj(4), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "1"), v_111)
# DecisionTree.add_obj(TreeObj(-1, "2"), v_111, False)
# DecisionTree.add_obj(TreeObj(-1, "5"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "6"), v_12, False)
# DecisionTree.add_obj(TreeObj(-1, "3"), v_112)
# DecisionTree.add_obj(TreeObj(-1, "4"), v_112, False)
#
# x = [0,0,1,1,0]
# res = DecisionTree.predict(root, x)
# print(res)
# print('indx', 'left', 'right', 'value', sep='   ')
# for i in DecisionTree.lst_obj:
#     print(i.indx, i.left, i.right, i.value, sep='   ', end='\n')
# print()
# [print(i) for i in DecisionTree.lst_obj]

# class PhoneBook:
#     def __init__(self):
#         self.lst_phone = []
#
#     def add_phone(self, phone):
#         self.lst_phone.append(phone)
#
#     def remove_phone(self, indx):
#         self.lst_phone.pop(indx)
#
#     def get_phone_list(self):
#         return self.lst_phone
#
#
# class PhoneNumber:
#
#     def __init__(self, number, fio):
#         self.number = number
#         self.fio = fio
#
#
#
# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
# p.add_phone(PhoneNumber(21345678901, "Панда"))
# phones = p.get_phone_list()
# print(phones)

# class Server:
#     COUNTER = 1
#
#     def __init__(self):
#         self.ip = self.COUNTER
#         self.buffer = []
#         self.counter()
#         self.router_connect = None
#
#     @classmethod
#     def counter(cls):
#         cls.COUNTER += 1
#
#     def send_data(self, data):
#         if self.router_connect:
#             self.router_connect.buffer.append(data)
#
#     def get_data(self):
#         temp = self.buffer[:]
#         self.buffer.clear()
#         return temp
#
#     def get_ip(self):
#         return self.ip
#
#
# class Router:
#     def __init__(self):
#         self.buffer = []
#         self.dict_server_connect = {}
#
#     def link(self, server):
#         self.dict_server_connect[server.ip] = server
#         server.router_connect = self
#
#     def unlink(self, server):
#         server.router_connect = None
#
#     def send_data(self):
#         for data in self.buffer:
#             for k, v in self.dict_server_connect.items():
#                 if data.ip == k:
#                     v.buffer.append(data)
#                     self.unlink(v)
#         self.dict_server_connect.clear()
#         self.buffer.clear()
#
#
# class Data:
#     def __init__(self, data, ip):
#         self.data = data
#         self.ip = ip
#
#
# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()

# class Integer:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         print(f'__set__:{self.name}={value}')
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p = Point3D(1,2,3)
#
# print(p.x)


# class FloatValue:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.check(value)
#         setattr(instance, self.name, value)
#
#     @classmethod
#     def check(cls, num):
#         if not type(num) is float:
#             raise TypeError("Присваивать можно только вещественный тип данных.")
#
#
# class Cell:
#     value = FloatValue()
#
#     def __init__(self, value):
#         FloatValue.check(value)
#         self._value = value
#
#
# class TableSheet:
#     def __init__(self, N, M):
#         self.N = N
#         self.M = M
#         self.cells = [[Cell(0.0) for _ in range(self.M)] for _ in range(self.N)]
#
#
# table = TableSheet(5, 3)
# count = 1
# for i in table.cells:
#     for j in i:
#         j.value = float(count)
#         count += 1


# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.__things = []
#         self.total_weight = 0
#
#     @property
#     def things(self):
#         return self.__things
#
#     def add_thing(self, thing):
#         if self.total_weight + thing.weight <= self.max_weight:
#             self.__things.append(thing)
#             self.total_weight += thing.weight
#
#     def remove_thing(self, indx):
#         self.__things.pop(indx)
#
#     def get_total_weight(self):
#         return self.total_weight

#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key, value = my_dict.pop-item()
# print(key, value)  # Вывод: последовательно выводится произвольная пара ключ-значение
# print(my_dict)
# print(my_dict.__dir__())

# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('вызов __new__ для' + str(cls))
#         return object.__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print('вызов __init__ для' + str(self))
#         self.x = x
#         self.y = y
#
#
# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('вызов __new__ для' + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print('вызов __init__ для' + str(self))
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)


# class A:
#     def __init__(self):
#         print('Constructor of class A')
#
# class B(A):
#     def __init__(self):
#         print('Constructor of class B')
#         # super().__init__()
#
# class C(B):
#     def __init__(self):
#         print('Constructor of class C')
#         object.__init__(self)

# class D(B, C):
#     def __init__(self):
#         print('Constructor of class D')
#         super().__init__()

# g = C()

# class Book:
#     def __init__(self, title='', author='', pages=0, year=0):
#         self._title = title
#         self._author = author
#         self._pages = pages
#         self._year = year
#
#     def __setattr__(self, key, value):
#         if key in ('_title', '_author'):
#             if isinstance(value, str):
#                 print('до')
#                 object.__setattr__(self, key, value)
#                 print('после')
#             else:
#                 raise TypeError("Неверный тип присваиваемых данных.")
#
#         if key in ('_pages', '_year'):
#             if isinstance(value, int):
#                 print('до')
#                 object.__setattr__(self, key, value)
#                 print('после')
#             else:
#                 raise TypeError("Неверный тип присваиваемых данных.")
#
#
# book = Book('Python ООП', 'Сергей Балакирев',123, 2022)
# print(book.__dict__)


