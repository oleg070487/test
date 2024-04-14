# print('Hello word')

# fruits = ['apple', 'banana', 'cherry']
#
# for index, value in enumerate(fruits):
#     print(f"Index: {index}, Value: {value}")

# x = 2100

# def is_leap_year(year):
#     if year % 4 == 0 or year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_leap_year(x))

# def is_leap_year(year):
#
#         return True if year % 4 == 0 or year % 400 == 0 and year % 100 != 0 else False
#
# print(is_leap_year(x))


# def divide(a, b):
#     if b == 0:
#         raise ValueError("Деление на ноль недопустимо")
#     return a / b
#
# # Пример вызова функции с возможным исключением
# try:
#     result = divide(10, 0)
# except ValueError as e:
#     print(f"Произошла ошибка: {e}")


# def divide(a, b):
#     result = a / b
#     return result
#
#
# # Пример вызова функции с возможным исключением
# try:
#     result = divide(10, 0)
# except ZeroDivisionError as e:
#     print(f"Произошла ошибка деления на ноль: {e}")

# h = ['h/g', 'h/e']
#
# n = (x.split('/') for x in h)
# print(type(n))

# def sort_by_value_and_index(arr):
#
#     return sorted(arr, key=lambda x: (x[0] + 1) * x[1])
#
# x = [23, 2, 3, 4, 5]
# result = sort_by_value_and_index(enumerate(x))
#
# out = []
# for i, v in result:
#     out.append(v)
#
# print(out)

# def sort_by_value_and_index(arr):
#     w = enumerate(arr)
#
#     res = list(sorted(w, key=lambda x: x[0]+1 *x[1]))
#     return res
#
#
#
#
# x = [23, 2, 3, 4, 5]
# print(sort_by_value_and_index(x))


# result = sort_by_value_and_index(enumerate(x))
#
# out = []
# for i, v in result:
#     out.append(v)
#
# print(out)

# !!!!!!!!!!!
# def sort_by_value_and_index(arr):
#     s = enumerate(arr, 1)
#     t = list(s)
#     print(t)
#     w = sorted(t, key=lambda elem: elem[0]*elem[1])
#     print(w)
#     res = []
#     for i in w:
#         res.append(i[1])
#     return res
#
# x = [23, 2, 3, 4, 5]
# print(sort_by_value_and_index(x))

# a = 45
# b = 5
#
# def f(x):
#     a = a+x
#     return a
# print(a)
# print(f(2))


# def my_function(x):
#     return x * 2
#
# # Проверим, что функция - объект
# print(type(my_function))  # <class 'function'>
#
# # Посмотрим на идентификатор функции
# print(id(my_function))
#
# # Выведем саму функцию
# print(my_function)
#
# def my_function(arg):
#     print(arg)
#
# my_function(42)
# my_function(print)

# my_list = [42, "hello", print]
#
# # Итерация по элементам списка
# for item in my_list:
#     # Проверка, является ли элемент функцией
#     if callable(item):
#         # Вызов функции
#         item("Function call")
#     else:
#         print(item)

# print_function = print
# print_function("Hello, World!")

# def create_function():
#     def inner_function():
#         print("Hello from inner function")
#     return inner_function
#
# new_function = create_function() # == inner_function
# # print(new_function)
# print(new_function())# ===inner_function()


# s = [1,2,3,4,56,8]
#
# print(s[::2])
# print(create_function())

# a = [1, 2, 3, 4, 5, 6]
# b = 'abcdef'
# res = zip(a,b)
# print(dict(res))

# x = []
#
# for i in range(20):
#     if i % 5 == 0:
#         x.append(i)
# print(x)

#
# x = (i for i in range(20) if i % 5 == 0)
# print(list(x))


# s = []
# for i in range(1, 21):
#     for j in range(1, 31):
#         s.append((i, j))
# print(s)
#
# s = [(i, j) for i in range(1, 21) for j in range(1, 31)]
# print(s)

# num = int(input("Enter a number between 1 and 12: "))
# for i in range(1, 13):
#     answer = i * num
#     print(i, "x", num, "=", answer)

# total = 0
# while total < 100:
#     num = int(input("Enter a number: "))
#     total = total + num
# print("The total is ", total)


# import random
# q = random.choice(['Орел', 'Решка'])
#
# user = input('Выберите "Орел" или "Решка": ')
#
# if q == user:
#     print("Вы выйграли!")
# else:
#     print("Вы проиграли, верный ответ " + q + "!")

# import turtle
# for i in range(0, 3):
#     turtle.right(36)
#     for i in range(0, 5):
#         turtle.forward(100)
#         turtle.right(72)
# turtle.exitonclick()


#
# import turtle
# turtle.left(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# turtle.forward(75)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(75)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(45)
# turtle.left(180)
# turtle.forward(45)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(75)
# turtle.hideturtle()
# turtle.exitonclick()


# word = input("Enter a word: ")
# length = len(word)
# num = 1
# for x in word:
#     position = length - num
#     letter = word[position]
#     print(letter)
#     num = num + 1

# word = input("Enter a word: ")
# res = word[::-1]
# for x in res:
#     print(x)


# x, y = [5,6,78,1], 'value'
# w, q = [5,6,78,1], 'index'
#
# def minimal(a,b):
#     if b == 'value':
#         return min(a)
#     if b == 'index':
#         return a.index(min(a))
# print(minimal(w,q))

# x = [4, 5, 7, 5, 4, 8]

# def func(arg):
#     res = []
#     for i in arg:
#         if arg.count(i) == 1:
#             res.append(i)
#     return sum(res)
#
# print(func(x))

# def func(arg):
#     return sum(i for i in arg if arg.count(i) == 1)
#
# print(func(x))

# x = "nit picking"
# def spoonerize(words):
#     res = words.split(' ')
#     res1 = res[1][0] + res[0][1:], res[0][0]+res[1][1:]
#     return " ".join(res1)
#
# print(spoonerize(x))

# x = 100
# def func(arg):
#     count = 0
#     for i in range(1, arg+1):
#         if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
#             count += 1
#     return count
#
# print(func(x))
# def func(arg):
#     return len([i for i in range(1, arg+1) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0])
#
# print(func(x))

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

from functools import reduce
# def func(arg):
#     list = []
#     i = -1
#     for el in arg:
#         i += 1
#         list.append(el[i])
#     return reduce(lambda x, y: x*y, list, 1)
# print(func(x))

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# def func(arg):
#     i = -1
#     res = 1
#     for el in arg:
#         i += 1
#         res *= el[i]
#     return res
# print(func(x))

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# from math import prod
# def func(arg):
#     return prod(arg[i][i] for i in range(len(arg)))
# print(func(x))
#

# x = 37
#
# def func(arg):
#     list = []
#     for i in range(1, arg):
#         if arg % i == 0:
#             list.append(i)
#     return True if sum(list) > arg else False
# print(func(x))


# x = 12
#
# def func(arg):
#     return True if sum([i for i in range(1, arg) if arg % i == 0]) > arg else False
#
# print(func(x))
#

# import math
#
# x = 0
# def is_square(n):
#     if n > 0:
#         return n % math.sqrt(n) == 0
#     elif n == 0:
#         return True
#     else:
#         return False
#
# print(is_square(x))

# x = "AAGTT"
# def DNA_strand(dna):
#     return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])
# print(DNA_strand(x))

# list = [4,1,6,2]
#
# x = list.sort()
#
# print(x)
# print(list)


# import math
# x = 625
#
# def func(arg):
#     y = math.sqrt(arg)
#     if arg % y == 0:
#         return int((y+1)**2)
#     else:
#         return -1
# print(func(x))


# import math
# x = 114
#
# def func(arg):
#     return int((math.sqrt(arg)+1)**2) if arg % math.sqrt(arg) == 0 else -1
# print(func(x))


# print(121**0.5)

# s = "aaaxbbbbyyhwawiwjjjwwm"
#
# def func(arg):
#     list = []
#     count = 0
#     for x in range(ord('a'), ord('m')+1):
#         list.append(chr(x))
#     for i in arg:
#         if i not in list:
#             count += 1
#     return str(count) + '/' + str(len(s))
# print(func(s))

# x,y,z = 1,2,3
# def is_triangle(a, b, c):
#     res = [a,b,c]
#     res.remove(max(res))
#     if sum(res) > max(a,b,c):
#         return True
#     else:
#         return False
#
# print(is_triangle(x,y,z))

# x = 16
#
# def func(arg):
#     list = []
#     for i in range(1, arg):
#         if i % 3 == 0 or i % 5 == 0:
#             list.append(i)
#     return sum(list)
#
# print(func(x))

# x = 16
# def func(arg):
#     return sum([i for i in range(1, arg) if i % 3 == 0 or i % 5 == 0])
# print(func(x))


# string = "Hey fellow warriors"
#
# def func(arg):
#     res = []
#     list = string.split()
#     for i in list:
#         if len(i) >= 5:
#             res.append(i[::-1])
#         else:
#             res.append(i)
#     return " ".join(res)
# print(func(string))

# string = "Hey fellow warriors"
#
# def func(arg):
#     return " ".join([i[::-1] if len(i) >= 5 else i for i in arg.split()])
# print(func(string))


# input_string = "AAGTT"
# translation_table = str.maketrans("ATCG", "TAGC")
# result = input_string.translate(translation_table)
# print(result)
# Вывод: TTCAA

# x =[0,1,1,0,0]
#
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i
# print(find_it(x))

# x =[0,1,1,0,0]

# def find_it(seq):
#     return [i for i in seq if seq.count(i) % 2 != 0][0]
# print(find_it(x))

# def likes(names):
#     match names:
#         case []: return 'no one likes this'
#         case [a]: return f'{a} likes this'
#         case [a, b]: return f'{a} and {b} like this'
#         case [a, b, c]: return f'{a}, {b} and {c} like this'
#         case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'

from functools import reduce
# x = 493193
#
# def func(arg):
#     while arg > 9:
#         new_list = []
#         for i in str(arg):
#             new_list.append(int(i))
#             arg = sum(new_list)
#     return arg
#
# print(func(x))


# def sum_digits(n):
#     # Суммировать цифры числа
#     digit_sum = sum(int(digit) for digit in str(n))
#
#     # Если сумма имеет более одной цифры, рекурсивно вызвать функцию
#     if digit_sum >= 10:
#         return sum_digits(digit_sum)
#     else:
#         return digit_sum
#


# x = 493193
# def digital_root(n):
#     while n>9:
#         n=sum(map(int,str(n)))
#     return n
#
# print(digital_root(x))

# x = 493193
#
# def digital_root(n):
# 	return n%9 or n and 9
#
# print(digital_root(x))

# x = 493193 % 9
# print(x)

# x = [1,2,3]
# y = [1,2]
#
# def func(a, b):
#     for i in a:
#         if i in b:
#             a.remove(i)
#     return a
# print(func(x,y))

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# w = ''.join(map(str, x))
# print(w)

# x = 493193
#
# res = bin(x).count('1')
# print(res)

# x = [2, 4, 0, 100, 4, 11, 2602, 36]
#
# def func(arg):
#     list1 = []
#     list2 = []
#     for i in arg:
#         if i % 2 == 0:
#             list1.append(i)
#         elif i % 2 != 0:
#             list2.append(i)
#     return list1[0] if len(list1) == 1 else list2[0]
#
#
# print(func(x))

# x = "Indivisibilities"
# def duplicate_count(text):
#     res = text.upper()
#     list = []
#     # return len([i for i in res if res.count(i)>1])
#     for i in res:
#         if res.count(i) > 1:
#             list.append(i)
#     return list
#
# print(duplicate_count(x))
#

# x = "recede"
# def duplicate_encode(word):
#     return ''.join([')' if word.lower().count(i) > 1 else '(' for i in word.lower()])
#
# print(duplicate_encode(x))

# x = ord('a')
# print(x)
#
# y = ord('z')
# print(y)
#
# res = y - x
# print(res)


import string

# def func(arg):
#     key = [str(i) for i in range(1, ord('z') - ord('a') + 2)]
#     value = [chr(j) for j in range(ord('a'), ord('z') + 1)]
#
#     res = dict(zip(key, value))
#     new_list = []
#     for i in arg.lower():
#         for k, v in res.items():
#             if v in i:
#                 new_list.append(k)
#     return ' '.join(new_list)

# x = "The sunset sets at twelve o' clock."
# result = func(x)
# print(result)
#
# # Должен вернуться "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for i in my_dict:
#     print(i)


# from functools import reduce
# x = 999
# def func(n):
#     count = 0
#     while n > 9:
#         n = reduce(lambda a, b: a * b, map(int,str(n)))
#         count += 1
#     return count
# print(func(x))

# from functools import reduce
# x = 999
# def func(n, count=0):
#     if n < 10:
#         return count
#     else:
#         new_n = reduce(lambda a, b: a * b, map(int, str(n)))
#         return func(new_n, count + 1)
# print(func(x))

# import re
# x = 'the-stealth_warrior'
#
# def func(arg):
#     word = re.split('[-_]', arg)
#     return word[0] + ''.join([i.capitalize() for i in word[1:]])
# print(func(x))

#
# x = 'is2 Thi1s T4est 3a'
#
# def func(arg):
#     res = {}
#     final = []
#     for i in x.split():
#         for j in i:
#             if j.isdigit():
#                 res[j] = i
#
#     new_dict =  dict(sorted(res.items(), key=lambda y: y[0]))
#     for v in new_dict.values():
#         final.append(v)
#     return " ".join(final)
#
#
#
# print(func(x))

# x = 'is2 Thi1s T4est 3a'
#
# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
#
# print(order(x))

# x = 153
#
# def narcissistic(value):
#     list1 = []
#     res = list(map(int, str(value)))
#     for i in res:
#         list1.append(i ** len(res))
#     return False if sum(list1) != value else True
#
#
# print(narcissistic(x))


# x = 153
#
#
# def narcissistic(value):
#     res = list(map(int, str(value)))
#     return False if sum(i**len(res) for i in res) != value else True
#
#
# print(narcissistic(x))

# x = 153
#
#
# def narcissistic(value):
#
#     return value == sum(int(i)**len(str(value)) for i in str(value))
#
#
# print(narcissistic(x))


# x, y = [1,1,1],10
#
# def func(arg1,arg2):
#     list_fib = arg1
#     count = 0
#     if arg2 > 0:
#         while count < arg2-3:
#             list_fib.append(sum(arg1[0+count:3+count]))
#             count += 1
#         return list_fib[:arg2]
#     elif arg2 == 0:
#         return []
#
# print(func(x,y))

# x, y = [1,1,1],10
#
# def func(arg1,arg2):
#     while len(arg1) < arg2:
#         arg1.append(sum(arg1[-3:]))
#     return arg1[:arg2]
#
# print(func(x,y))
#

# x = 'AAAABBBCCDAABBB'
#
#
# def unique_in_order(sequence):
#     res = []
#     if len(sequence)>0:
#         for i in range(len(sequence)-1):
#             if sequence[i] != sequence[i+1]:
#                 res.append(sequence[i])
#         res.append(sequence[-1])
#         return res
#     else:
#         return []
# print(unique_in_order(x))

# x = 'AAAABBBCCDAABBB'
# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result
#
# print(unique_in_order(x))

# x = 'AAAABBBCCDAABBB'
# def unique_in_order(iterable):
#     res = []
#     for item in iterable:
#         if len(res) == 0 or item != res[-1]:
#             res.append(item)
#     return res
# print(unique_in_order(x))

# x, y = 46288, 3
#
#
# def dig_pow(n, p):
#     res = 0
#     for i in str(n):
#         res += int(i) ** p
#         p += 1
#     if res % n == 0:
#         return res // n
#
# print(dig_pow(x,y))
#


# x = '.-'
#
# MORSE_CODE ={'.-':'A'}
# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
#
# print(decodeMorse(x))
#
# def decodeMorse(morseCode):
#     CHARS = " "
#     WORDS = "   "
#     lst = []
#     for word in morseCode.strip().split(WORDS):
#         wordLst = []
#         for character in word.split(CHARS):
#             wordLst.append("".join(MORSE_CODE[character]))
#         lst.append("".join(wordLst))
#     return " ".join(lst)

# x = "This isn't a pangram!"
#
# def is_pangram(s):
#     alf = [chr(char) for char in range(65, 91)]
#     for i in alf:
#         if i not in s.upper():
#             return False
#
#     return True
#
# print(is_pangram(x))

# x = [1,2,3,4,3,2,1]
#
# def func(arg):
#     for i in range(len(arg)):
#         if sum(arg[:i]) == sum(arg[i+1:]):
#             return i
#
#
#
# print(func(x))

# a = 7
# b = a
# print(id(a))
# print(id(b))

# x = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#
# def func(arg):
#     list_odd = []
#     list_sorted = []
#     for i in arg:
#         if i % 2 != 0:
#             list_odd.append(i)
#     list_odd = sorted(list_odd)
#     index = 0
#     for i in arg:
#         if i % 2 != 0:
#             list_sorted.append(list_odd[index])
#             index += 1
#         else:
#             list_sorted.append(i)
#     return list_sorted
#
# print(func(x))


# list1 = [1,2,3,3]
# list2 = [1,2,3,4,5]
# print(list(zip(list1,list2)))

import string

# x = ['O','Q','R','S']
#
#
# import string
# def find_missing_letter(chars):
#     alf_lower = string.ascii_lowercase
#     alf_upper = alf_lower.upper()
#     string_correct = ''
#     alf = None
#     if chars[0].islower():
#         alf = alf_lower
#     elif chars[0].isupper():
#         alf = alf_upper
#     if chars[0] in alf:
#         string_correct = string_correct + alf[alf.index(chars[0]):alf.index(chars[0])+len(chars)+1]
#     for i in string_correct:
#         if i not in chars:
#             return i
#
# print(find_missing_letter(x))
#
#
# def find_missing_letter(chars):
#     for i in range(len(chars) - 1):
#         if ord(chars[i]) != ord(chars[i + 1]) - 1:
#             return chr(ord(chars[i]) + 1)

# x = 2
# def tower_builder(n_floors):
#     result = []
#     count = 0
#     count1 = n_floors-1
#     for i in range(1, n_floors + 1):
#         result.append(count1 * ' ' + count * '*' + '*' +count * '*' + count1 * ' ')
#         count += 1
#         count1 -= 1
#     return result
#
# print(tower_builder(x))


# input = 'man i need a taxi up to ubud'
#
# def high(x):
#     return max(x, key = lambda y: sum([ord(j) for i in y.split() for j in i ])
# print(high(input))

# import string
# input = 'bb d'
#
# def high(x):
#     alf = string.ascii_lowercase
#     list_split = x.split()
#     dict1 = {}
#     list_sum = []
#     for i, e in enumerate(alf):
#         dict1[e] = i+1   # или так:   dict1.setdefault(e, i+1)
#     for i in list_split:
#         sum_char = 0
#         for j in i:
#             sum_char += dict1[j]
#         list_sum.append(sum_char)
#     return list_split[list_sum.index(max(list_sum))]
#
# print(high(input))
#
# print(ord('a'))

#
# import string
# alf = string.ascii_lowercase
#
# dict1 = {}
#
# for i, e in enumerate(alf):
#     dict1.setdefault(e, i+1)
# print(dict1)
# del dict1['a']
# print(dict1)
#
# x = []
#
# print(x.count(1))
# x = [-2,5]
# y = -10
#
# print(-2 >= y <= 5)
# print(ord('Ф'))
#
# msg ='abracadabra'
#
# print(msg.count('ra',4,11))
#
# x = 779689
# def func(arg):
#     for i in range(2, 20):
#         if arg % i == 0 or arg < 0:
#             if i == arg:
#                 continue
#
#             return False
#     else:
#         return True
# print(func(x))

# x = [1,2,3]
#
# # type = 7
# print(type(x))
#
# print(type(21/4))

# ввод целого числа


# здесь продолжите программу
# print(max(map(int, input().split())))
# import math
# # ввод данных
# a, b = map(int, input().split())
#
# # здесь продолжите программу
# print(round((math.sqrt(a**2 + b**2)), 2))

# import math
# # ввод данных
# n, k = map(int, input().split())
#
# # здесь продолжите программу
# print(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

# n, m = map(int, input().split())
#
# # здесь продолжите программу
# print(round((n + m)/20))
#
# a, b = map(int, input().split())
#
# print(sum([a, b]))


# import random
# selection_of_quantities_bichs = int(input('Сколько шлюх желаете заказать? '))
#
# all_bichs = {
#             'Masha': 40,
#             'Janna': 50,
#             'Dasha': 65,
#             'Violeta': 45,
#             'Snejana': 70,
#             }
#
# all_1 = [i for i in all_bichs.keys()]
# select = []
# while len(select) < selection_of_quantities_bichs:
#     x = random.choice(all_1)
#     if x not in select:
#         select.append(x)
# print()
# print('К Вам выехали шлюхи:', ', '.join(select))
# print(f'Всего к оплате: {sum(all_bichs[i] for i in select)}$')


# import random
#
# # список автомобилей и их цен за день аренды
# cars = {
#     "Toyota Corolla": 50,
#     "Honda Civic": 60,
#     "Ford Mustang": 80,
#     "Nissan Altima": 55,
#     "BMW X5": 120,
#     "Tesla Model S": 200,
# }
#
# # получить количество автомобилей, которые пользователь хочет арендовать
# num_cars = int(input("Сколько автомобилей вы хотите арендовать? "))
#
# # случайно выбрать имена автомобилей из списка
# car_names = random.sample(list(cars.keys()), num_cars)
#
# # вычислить общую стоимость аренды
# total_cost = sum(cars[name] for name in car_names)
#
# # вывести имена выбранных автомобилей и общую стоимость аренды
# print("Выбранные автомобили:")
# for name in car_names:
#     print("- " + name)
# print("Общая стоимость аренды: $" + str(total_cost))
#
#


# a, b, c = map(int, input().split())
#
# print(a < b + c and b < a + c and c < b + a)

#
# s1, s2 = input(), input()
#
# print(s1, s2)


# s1, s2 = input().split()
#
# print(s1)


# print((cities := input().split())[-1])


# book_info = input(), input(), int(input()), float(input())
# book_info = list(book_info)
# print(book_info)

# list_input = list(map(int, input().split()))
# new_list = []
# new_list.append(str(max(list_input)))
# new_list.append(str(min(list_input)))
# new_list.append(str(sum(list_input)))
# print(' '.join(new_list))

# list1=[1,2,3,4,5,6,7]
#
# list2 =[67,54,78]
# print(list1+list2)
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# n=reversed(m[2:7])
# print(n)
#
# phone = list(input())
# print(phone)
# del phone[0]
# print(phone)
# phone[0] = '8'
# print()
# phone.remove('-')
# phone.remove('-')
# print(''.join(phone))

# x = [1,2,3,4,56]
# print(x[:-1])

# l = input().split(), input().split(), input().split()
# new_list = list(l)
# print(new_list)

# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#      ["Я", "Python", "выучил", "с", "каналом"],
#      ["Балакирев", "что", "раздавал?"]]

# здесь продолжайте программу
# new_list = t[0] + t[1] + t[2]
# print(new_list)
# print('дядя' in new_list)

# a, b, c = map(int, input().split())
# list1 = ('NO','YES')
# print(list1[c**2 == a**2 + b**2])
# print(type(list1))

# a = '324454'
# res = a.split('')
# print(res)

# data = input()
# x = list(data)
# print(x)

# word = input()
# print('НДЕАТ'['t' in word and 'h' in word and 'o' in word::2])

# data =int(list(input()))
# print(data)

# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
#
# x = m.split('\n')
# print(x)
#
# a, b, c = 8, 11, -1
#
# if a < b:
#     if a < c:
#         print(a)
#     elif c < b:
#         print(c)
# else:
#     if b < c:
#         print(b)
#     else:
#          print(c)


# put your python code here
# x = int(input())
# if x % 2 != 0 and 0 < x < 8:
#     print('31')
# elif x % 2 == 0 and 7 < x < 13:
#     print('31')
# elif x % 2 == 0 and 2 < x < 8:
#     print('30')
# elif x % 2 != 0 and 7 < x < 13:
#     print('30')
# elif x == 2:
#     print('28')


# x = float(input())
# n = 2
# while n < 11:
#     print(round(x * n, 1))
#     n += 1

# x = input()
# while '--' in x:
#     x = x.replace('--', '-')
# print(x)

# put your python code here
# x = input()
# res = 1
# n = 1
# while n <= len(x):
#     res *= int(x[n-1])
#     n += 1
# print(res)

# x = int(input())
# i = 0
# summ = 1
# fibonaci = '1 '
#
# while i < x:
#     summ += i
#     i += 1
#     fibonaci += str(summ) + ' '
#
# print(fibonaci)

# print(*range(231, 1000, 141))


# p = [0] * 10
# while p.count(1) < 5:
#     x = int(input())
#     if p[x] == 1:
#         continue
#     p[x] = 1
# print(*p)


# x = 1
# res = 1
# while x != 0:
#     x = int(input())
#     if x < 0:
#         continue
#     res *= x
# print(res)


# students = input().lower().split()
# i = 0
# while i < len(students):
#     if students[i][0] == students[i][-1]:
#         print('ДА')
#         break
#     i += 1
# else:
#     print('НЕТ')


# print(('НЕТ', 'ДА')[any(i[0] == i[-1] for i in input().lower().split())])

# a = int(input())
# b = int(a ** 0.5 // 1)
# print(b + 1)
# print(b)

# print(range(11))

# cities = input().lower().strip('ьыъ').split()
# res = None
# for i in range(len(cities) - 1):
#     if cities[i][-1] != cities[i + 1][0]:
#         res = 'НЕТ'
# else:
#     res = 'ДА'
# print(res)
#
# print(cities)
#

# num = list(input())
# for i, v in enumerate(num[2:], 2):
#     if v in '0123456789':
#         num[i] = 'x'
# print(num)
# if num == list('+7(xxx)xxx-xx-xx'):
#     print('ДА')
# else:
#     print('НЕТ')

# num = list(input())
# for i, v in enumerate(num[2:], 2):
#     if v.isdigit():
#         num[i] = 'x'
# if num == list('+7(xxx)xxx-xx-xx'):
#     print('ДА')
# else:
#     print('НЕТ')
#
# x = '+7(123)456-78-99'

# ex = input().replace(' ', '').replace('+', '_+').replace('-', '_-').split('_')
# res = 0
# for i, v in enumerate(ex):
#     if '+' in v:
#         res = (res if res != 0 else int(ex[i-1])) + int(ex[i][1:])
#     elif '-' in v:
#         res = (res if res != 0 else int(ex[i-1])) - int(ex[i][1:])
# print(res)
#
#
# x = '10+25 - 12'

# x = list(map(float, input().split()))
# min = None
#
# for i, v  in enumerate(x[:-1]):
#     if v < x[i+1]:
#         min = v
#     else:
#         min = x[i+1]
# print(min)


# n = int(input())
# new = []
# for i in range(n):
#     new.append([1] * n)
#
# for i in range(n):
#     for j in range(3, 4):
#         new[i][j] = 5
# for i in new:
#     print(*i)
#
# print(id(new))
# print(id(new[0]))
# print(id(new[1]))

# n = 4
# lst = [[1] * n] * n
# print(id(lst))
# print(id(lst[0]))
# print(id(lst[1]))

# lst2 = [[1] * n for _ in range(n)]
# print(id(lst2))
# print(id(lst2[0]))
# print(id(lst2[1]))


# n = int(input())
#
# lst = [[1] * n] * n
# lst[0][n-1] = 5
#
# for i, v  in enumerate(lst):
#     print(*lst[i])

# x = int(input())
#
# for i in range(2, x):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')
# import time
#
# lst_in = [[1, 0, 0, 0, 0],
#           [0, 0, 1, 0, 1],
#           [0, 1, 0, 0, 0],
#           [0, 1, 0, 1, 0],
#           [0, 0, 0, 0, 0]]

# start2 = time.time()
#
# flag = True
# for i in range(4):
#     for j in range(4):
#         summ = lst_in[i][j] + lst_in[i][j+1] + lst_in[i+1][j] + lst_in[i+1][j+1]
#         if summ > 1:
#             flag = False
#             break
#     else:
#         continue
#     break
# print('ДА' if flag == True else 'НЕТ')

# stop2 = time.time()

# start1 = time.time()
# flag = True
#
# for i in range(len(lst_in)-1):
#     for j in range(len(lst_in)-1):
#         if (lst_in[i][j] + lst_in[i][j+1] + lst_in[i+1][j] + lst_in[i+1][j+1]) > 1:
#             flag = False
#             break
#
# print(["НЕТ", "ДА"][flag])
# stop1 = time.time()
#
# print(stop1-start1)
# print(stop2-start2)


# lst_in = [[2, 3, 4, 5, 6],
#           [3, 2, 7, 8, 9],
#           [4, 7, 2, 0, 4],
#           [5, 8, 0, 2, 1],
#           [6, 9, 4, 1, 2]]

# flag = True
# for i in range(len(lst_in)):
#     for j in range(i+1, len(lst_in)):
#         if lst_in[i][j] != lst_in[j][i]:
#             flag = False
#             break
#     else:
#         continue
#     break
# print('ДА'if flag == True else 'НЕТ')

# lst_in = [[2, 3, 4, 5, 6],
#           [3, 2, 7, 8, 9],
#           [4, 7, 2, 0, 4],
#           [5, 8, 0, 2, 1],
#           [6, 9, 4, 1, 2]]
# flag = True
# for i, v in enumerate(lst_in):
#     sum_row = sum(v)
#     sum_col = 0
#     for j, w in enumerate(v):
#         sum_col += lst_in[j][i]
#     if sum_row != sum_col:
#         flag = False
#         break
# print('ДА'if flag == True else 'НЕТ')


# x = [8, 11, -53, 2, 10, 11]

# for i in range(len(x)):
#     minimal = x[i]
#     for j, v in enumerate(x[i+1:], start=i+1):
#         if v < minimal:
#             minimal = v
#             min_index = j
#     x[i], x[min_index] = x[min_index], x[i]
# print(*x)

# алгоритм сортировки выбором!!!
# lst = [8, 11, -53, 2, 10, 11]
# n = len(lst)

# for i in range(n - 1):
#     minimal = lst[i]
#     index_minimal_number = i
#     for j in range(i + 1, n):
#         if lst[j] < minimal:
#             minimal = lst[j]
#             index_minimal_number = j
#     if index_minimal_number != i:
#         lst[i], lst[index_minimal_number] = lst[index_minimal_number], lst[i]
#
#         """ или так """
#         temporary_variable = lst[index_minimal_number]
#         lst[index_minimal_number] = lst[i]
#         lst[i] = temporary_variable
#
# print(lst)

# l = [8, 11, -53, 2, 10, 11]
#
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] < l[j]:
#             l[i], l[j] = l[j], l[i]
# print(*l)


# алгоритм сортировки вставками
# lst = [8, 11, -53, 2, 10, 11]
#
# for i in range(len(lst)):
#     for j in range(i, len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
# print(*lst)

# s = [8, 11, -53, 2, 10, 11]
# for i in range(len(s) - 1):
#     for j in range(i+1, len(s)):
#         if s[j] < s[i]:
#             s[j], s[i] = s[i], s[j]
# print(*s)


# lst = [-53, 2, 8, 10, 11, 11]
# for i in range(len(lst), 0, -1):
#     ordered = True
#     for j in range(1, i):
#         if lst[j - 1] > lst[j]:
#             lst[j - 1], lst[j], ordered = lst[j], lst[j - 1], False
#     if ordered:
#         break
# print(lst)

# many = [1]
# res = 1
# for i in range(6):
#     res *= 2
#     many.append(res)
# x = 221
# res_many = []
# for j in many[::-1]:
#     q = x // j
#     x %= j
#     res_many += [j]*q
#
# print(*res_many)

# from time import time
#
# start_1 = time()
#
# n = 221
# lst = []
# for i in [64, 32, 16, 8, 4, 2, 1]:
#     k = n // i
#     lst += [i] * k
#     n -= i * k
# stop_1 = time()
#
# start_2 = time()
# n = 221
# s = ''
# for i in (64, 32, 16, 8, 4, 2, 1):
#     k = n // i
#     s += f'{i} ' * k
#     n -= i * k
#
# print(s)
# stop_2 = time()
#
# res1 = start_1
# print(res1)
# res2 = start_2
# print(res2)



# from time import time
#
# start_1 = time()
# N = 1000
# P = []
# for k in range(1, N):
#     P.append([1]*k)
# print(P)
# n = len(P)
# for i in range(2, n):
#     for j in range(1, i):
#         P[i][j] = P[i-1][j-1]+P[i-1][j]
#
# print(P)
#
# stop_1 = time()
#
# start_2 = time()
#
#
#
# N = 1000
# P = []
#
# for i in range(N):
#     row = [1] * (i+1)
#     for j in range(i+1):
#         if j != 0 and j != i:
#             row[j] = P[i-1][j] + P[i-1][j-1]
#     P.append(row)
# print(P)
#
# stop_2 = time()
#
# res1 = stop_1 -start_1
# print(res1)
# res2 = stop_2 -start_2
# print(res2)



# x = [1,2,3,4,5]
# for i in range(4, -1, -1):
#
#     print(x[i])


# lst = [[a for a in range(3)] for b in range(4)]
# lst1 = [a for b in range(4) for a in range(3)]
# print(lst)
# print(lst1)

# print(round(9**0.5))
# x = list(map(int, input().split()))
# n = round(len(x)**0.5)
#
# lst = [[v for v in x[i:i+n]] for i in range(0, len(x), 3)]
# print(lst)

# lst = list(map(int, input().split()))
# n = int(len(lst) ** .5)
# print([[lst[n * i + j] for j in range(n)] for i in range(n)])

# d = {1:2, 3:4}
# print(d)

# x = input().split()
# res = []
# for i in x:
#     a, b = i.split('=')
#     res.append([a, int(b)])
# d = dict(res)
# print(d)



# x = input().split()
#
# d = [[int(v) if j == 1 else v for j, v in enumerate(i.split('='))] for i in x]
# print(dict(d))

# x = [1, 2, 3]
# print(x[:-2])


# g =[u ** 2 for u in range(1, 6)]
# print(g)



# d = dict(i.split('=') for i in input().split())
# for i in ['False', '3']:
#     if i in d:
#         del d[i]
# print(d)
# print(*sorted(d.items()))

# x = input().split()
# d = {}
#
# for j in x:
#     if j[:2] not in d:
#         d[j[:2]] = [j]
#     else:
#         d[j[:2]] += [j]
#
# print(d)


# lst_key = []
# for x in range(32):
#     lst_key.append(chr(ord('А') + x))
# lst_key += [' ']
#
# morze = dict.fromkeys(lst_key)
# d = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
#      'Е': '.', 'Ж': '...-', 'З': ' --..', 'И': '..', 'Й': '.---',
#      'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
#      'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
#      'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
#      'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
#      'Ю': '..--', 'Я': '.-.-', ' ': '-...-'}
#
#
# print(morze)


# morze = {'а': '.-', 'б': '-...', 'в': '.--'}
#
# strijjf = ''
#
# translation_table = strijjf.maketrans(morze)
# print(translation_table)


# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
#
# sorted_dict = dict(sorted(things.items(), key=lambda item: item[1], reverse=True))
# x = int(input()) * 1000
# weight = 0
# bag_dict = {}
# for key, value in sorted_dict.items():
#     weight += value
#     if weight <= x:
#         bag_dict[key] = value
#     else:
#         weight -= value
#         continue
# print(*bag_dict.keys())
#

# lst_in = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12]]
#
# lst = []
# for i in range(len(lst_in[0])):
#     row = []
#     for j in range(len(lst_in)):
#         row += [lst_in[j][i]]
#     lst.append(row)
# print(lst)


# l = [[2, 3, 4, 5],
#      [9, 2, 6, 7],
#      [10, 11, 2, 8],
#      [12, 13, 14, 2]]
# for i in l:
#     print(*i)
#
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         l[i][j], l[j][i] = l[j][i], l[i][j]
#
#
# for i in l:
#     print(*i)

# s1 = {1,2}
# s2 ={2,}
# s = s1 + s2
# print(s)


# lst_in = ["Пушкин: Сказака о рыбаке и рыбке",
#           "Есенин: Письмо к женщине",
#           "Тургенев: Муму",
#           "Пушкин: Евгений Онегин",
#           "Есенин: Русь"]
# lst_tuple=[x.split(': ') for x in lst_in]
#
# for k in lst_tuple:
#     print(k)
# d = {}
#
# for line in lst_in:
#     author, book = line.split(': ')
#     if author not in d:
#         d[author] = set()
#     d[author].add(book)
# print(d)
#
#


# def check_email(e):
#     flag = True
#     l = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(10)] + ['_', '@', '.']
#     if '@' not in e and '.' not in e:
#         flag = False
#     for i in e:
#         if i.lower() not in l:
#             flag = False
# import string
# def func(a):
#     email_adress = '@' + '.' + string.ascii_lowercase + string.ascii_uppercase + string.digits + '_'
#     for i in a:
#         if i not in email_adress and '@' not in email_adress and '.' not in email_adress and a.count('@') != a.count('.') != a.count('_') != 1:
#             return 'НЕТ'
#         return 'ДА'


# lst_in = ["Пушкин: Сказака о рыбаке и рыбке",
#           "Есенин: Письмо к женщине",
#           "Тургенев: Муму",
#           "Пушкин: Евгений Онегин",
#           "Есенин: Русь"]
# d = {}
#
# for line in lst_in:
#     author, book = line.split(': ')
#     d[author] = d.get(author, set()) | {book}
# print(d)


# lst_in = ["Пушкин: Сказака о рыбаке и рыбке",
#           "Есенин: Письмо к женщине",
#           "Тургенев: Муму",
#           "Пушкин: Евгений Онегин",
#           "Есенин: Русь"]
# d = {}
#
# for line in lst_in:
#     author, book = line.split(': ')
#     d.setdefault(author, set()).add(book)
# print(d)



# import time
# def func1():
#     l = [x for x in range(1000000)]
#     print(*l, sep='\n')
#     return 'func1'
#
# def func2():
#     [print(x) for x in range(1000000)]
#     return 'func2'
#
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

# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     return a
#
# print(get_nod(18, 24))

# def get_nod(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# print(get_nod(18, 24))


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


# здесь продолжайте программу


# def translate_str(a, sep='-'):
#     res = ''
#     for i in a.lower():
#         if i in t:
#             res += t[i]
#         elif i == ' ':
#             res += sep
#         else:
#             res += i
#
#     return res
#
#
# print(translate_str(input()))
# print(translate_str(input(), sep='+'))

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу

# def func(s, sep='-'):
#     return ''.join([t[i] if i in t else i for i in s.replace(' ', sep)])
#
# s = input().lower()
# print(func(s))
# print(func(s, sep='+'))

# def get_biggest_city(*args):
#     for city in args:
#         if len(city) == max([len(i) for i in args]):
#             return city

# l = [[1, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0],
#      [0, 1, 0, 1, 0],
#      [0, 0, 0, 0, 0]]
#
#
# for i in range(len(l)-1):
#      for j in range(len(l)-1):
#           if l[i][j] + l[i][j+1] + l[i+1][j] + l[i+1][j+1] > 1:
#                print(False)
#                break
#      else:
#           continue
#      break
# else:
#      print(True)


# l = [[1, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0],
#      [0, 1, 0, 1, 0],
#      [0, 0, 0, 0, 0]]
#
# def is_isolate(l): # функция которая проверяет сумму всех элементов
#      return False if sum(l) > 1 else True
# def verify(x):
#      # добавляем нули по периметру матрицы:
#      # сначала создаем новый список только с нулями
#      l2 = [[0] * 7 for _ in range(7)]
#      # потом вставляем единицы из исходного списка по нужным индексам
#      for k in range(len(x)):
#           for v in range(len(x)):
#                if x[k][v] == 1:
#                     l2[k + 1][v + 1] = 1
#      # находим единицы в нашей новой матрице
#      for i in range(len(l2)):
#           for j in range(len(l2)):
#                if l2[i][j] == 1:
#                     lst = [] # если находим '1' создаем временный список из элеметов во круг единицы и самой единыцы (квадрат 3 x 3)
#                     for m in range(i - 1, i + 2):
#                          for n in range(j - 1, j + 2):
#                               lst.append(l2[m][n])
#                     res = is_isolate(lst) # передаем этот список в вспомогательную функцию которая проверяет сумму всех элементов
#                     if res == False:
#                          return res # если вспомогательнуя функция возвращает False тогда и основная возвращает False и прекращает работу
#      else:
#           return True # если циклы заверщаються штатно тогда основная функция возвращает True
# print(verify(l))

# lst = [[1, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0],
#      [0, 1, 0, 1, 0],
#      [0, 0, 0, 0, 0]]

# def verify(lst):
#     #расширяю матрицу нулями, чтобы не искать граничные индексы
#     lst.insert(0, [0] * len(lst))
#     lst.append([0] * (len(lst)-1))
#     for li in lst:
#         li.insert(0, 0)
#         li.append(0)
#     #ищу
#     for i, li in enumerate(lst):
#         if sum(li) > 0:
#             for j, nj in enumerate(li):
#                 if nj == 1:
#                     if not is_isolat(i,j,lst):
#                         return False
#     return True
#
# def is_isolat(i1, j1, lst):
#     sm = sum([sum(l[j1-1:j1+2]) for l in lst[i1-1:i1+2]])
#     return True if sm == 1 else False
# print(verify(lst))


# def str_min(s1, s2):
#      return min(s1, s2)
# def str_min3(s1, s2, s3):
#      s_min = str_min(s1, s2)
#      if s_min > s3:
#           return s_min
#      else:
#           return s3
#
#
# def str_min4(s1, s2, s3, s4):
#      s_min = str_min3(s1, s2, s3)
#      if s_min > s4:
#           return s_min
#      else:
#           return s4
#
# l1 = 'r'
# l2 = 'rjjj'
# l3 = 'r'
# l4 = 'efe'
#
# print(str_min(l1,l2))


# lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# # здесь продолжайте программу (используйте список lst_in и menu)
#
# menu_2 = {}
# for i in lst_in:
#     k, v = i.split("=")
#     menu_2[k] = v
#
# menu = dict(**menu, **menu_2)
# # print(menu)

# d111 = [pair.split('=') for pair in lst_in]
# print(d111)
#
# print(d)


# def fact(n): # рекурсивная функция
#      if n <= 0:
#           return 1
#      else:
#           return n * fact(n-1)
# print(fact(6))
#
# def func1(n): # то же самое но с использованием цикла а не рекурсии
#      res = 1
#      if n == 0:
#           return 1
#      else:
#           while n > 0:
#                res *= n
#                n = n-1
#      return res
#
# print(func1(6))


# x = list(map(int, input().split()))
#
# a = len(x)-1
# def summa(l, n):
#      s = 0
#      if n >= 0:
#          print('do', l[n])
#          s = l[n] + summa(l, n - 1)
#          print('posle', l[n])
#      return s
#
#
# print(summa(x, a))


# def get_rec_sum(nums):
#     if nums:
#         print(nums[0])
#         return nums[0] + get_rec_sum(nums[1:])
#     return 0
#
#
# nums = [int(x) for x in input().split()]
# print(get_rec_sum(nums))


# l = [8, 11, -5, 4, 3]
#
# a = len(l)-1
# def summa(n):
#      if n >= 0:
#          return l[n] + summa(n-1)
#      else:
#         return 0
#
# print(summa(a))

# l = [8, 11, -5, 4, 3]
# a = len(l)-1
# def summa(l, n):
#      s = 0
#      if n >= 0:
#          print('do', l[n])
#          s = l[n] + summa(l, n - 1)
#          print('posle', l[n])
#      return s
#
# #
# print(summa(l, a))

# N = 7
#
# def fibonaci():
#     f = [1, 1]
#     while len(f) < 7:
#         f.append(f[-2]+f[-1])
#     return f
# print(fibonaci(N))

# N = 7
#
# def fibonaci(n, f=[1,1]):
#     if len(f) < n:
#         return [f[n-1]+f[n-2]] + fibonaci(n-1, f)
#     return f
# print(fibonaci(N))
#

# lst = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
#
# # здесь продолжайте программу
# def get_line_list(d, a=[]):
#     for i in d:
#         if type(i) == list:
#             get_line_list(i, a)
#         else:
#             a.append(i)
#     return a
#
# print(get_line_list(lst))

# N = int(input())

# def get_path(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return get_path(n-1) + get_path(n-2)
#
# print(get_path(4))


# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return


# здесь продолжайте программу

# l = [5, 4, -3, 4, 5, -24, -6, 9, 0]
#
# lst = filter_lst(l, key=lambda x: True)
# print(*lst)
# lst1 = filter_lst(l, key=lambda x: x < 0)
# print(*lst1)
# lst2 = filter_lst(l, key=lambda x: x >= 0)
# print(*lst2)
# lst3 = filter_lst(l, key=lambda x: x >= 3 and x <= 6)
# print(*lst3)


# l = [11, 12, 13, 15]
#
# l2 = [-6, 11,16]
#
# def merge_two_lists(a, b):
#     res = []
#     while a and b:
#         res += [a.pop(0) if a[0] < b[0] else b.pop(0)]
#     return res + a + b
# print(merge_two_lists(l, l2))

# def func_union(lst1, lst2):
#     lst_res = []
#     i_1 = 0
#     i_2 = 0
#     for _ in range(len(lst1)+len(lst2)):
#         if lst1[i_1] < lst2[i_2]:
#             lst_res.append(lst1[i_1])
#             if i_1 < len(lst1)-1:
#                 i_1 += 1
#             else:
#                 for i in lst2[i_2:]:
#                     lst_res.append(i)
#                 break
#         else:
#             lst_res.append(lst2[i_2])
#             if i_2 < len(lst2) - 1:
#                 i_2 += 1
#             else:
#                 for i in lst1[i_1:]:
#                     lst_res.append(i)
#                 break
#     return lst_res
#
# # print(func_union(l, l2))
#
# def func_recursion(lll):
#
#     if len(lll) < 2:
#         return lll
#     else:
#         i = len(lll) // 2
#         l_1 = lll[:i]
#         l_2 = lll[i:]
#         return func_union(func_recursion(l_1), func_recursion(l_2))
#
# s = [8, 11, -6, 3, 0, 1, 1]
#
# print(func_recursion(s))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(1,2)
# print(id(pt))

# l = [1,2,3,4]
# print(l[-1:])
# l.pop()

# from string import ascii_lowercase, ascii_uppercase, digits
#
# print(ascii_lowercase)

# strarr = ["zone", "abigail", "theta", "form", "libe", "zas"]
#
# n = -2
#
# def longest_consec(strarr, k):
#     result = ''
#     print(k)
#     print(len(strarr))
#     if len(strarr) == 0 or k > len(strarr) or k < 0:
#         return result
#     else:
#         for i in range(len(strarr)-k+1):
#             res = ''.join(strarr[i:i+k])
#             if len(res) > len(result):
#                 result = res
#         return result

# print(longest_consec(strarr, n))



