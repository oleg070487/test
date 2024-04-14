import sys
import time
# def func1():
#     l = [x for x in range(1000000)]
#     print(*l, sep='\n')
#     return 'func1'
#
# def func2():
#     [print(x) for x in range(1000000)]
#     return 'func2'

# def is_time(a):
#     start1 = time.time()
#     name = a()
#     stop2 = time.time()
#     return f'{name} = {stop2-start1} сек'
#
#
#
# res1 = is_time(func1)
# res2 = is_time(func2)
#
# print(res1)
# print(res2)
# import pprint
import sys
# pprint.pprint(sys.path)
# from os import *
# pprint.pprint(locals())

# import tkinter as tk
#
# root = tk.Tk()
# root.geometry('500x500')
#
# radio_var = tk.StringVar(value=None)
#
#
# lab = tk.Label(root, text='radio:')
# lab.pack()
# radio = tk.Radiobutton(root, text='min', variable=radio_var, value ='+')
# radio1 = tk.Radiobutton(root, text='max', variable=radio_var, value ='-' )
# radio2 = tk.Radiobutton(root, text='NO', variable=radio_var, value ='no')
#
# radio.pack()
# radio1.pack()
# radio2.pack()
#
#
# root.mainloop()

# res = [[1 for j in range(3)]for i in range(3)]
#
# for i in res:
#     i.insert(0, 0)
#     i.append(0)
# res.insert(0, [0 for _ in range(len(res[0]))])
# res.append([0 for _ in range(len(res[0]))])
# [print(*i) for i in res]
#
# res_new = []
# for i in range(1, 3):
#     res_temp = []
#     for j in range(1, 3):
#         res_temp.append(res[i][j])
#     res_new.append(res_temp)
#
# print()
# [print(*i) for i in res_new]

# print(hex(255).replace('0x', ''))
# print(hex(255))


# from decimal import Decimal
#
# x = 4.556
# y = 1.1
#
# print(round(x/y, 15))
# print(round(Decimal(x)/Decimal(y), 15))


# import time


# class Timer:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         self.func(*args, **kwargs)
#         finish = time.time()
#         print(f'Время работы функции {finish - start}')
#
# @Timer
# def calculate():
#     for i in range(10_000_000):
#         2 ** 100
#
# calculate()
