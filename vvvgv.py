# import os
#
# # Указываем начальную директорию для обхода
# start_dir = os.getcwd()
#
# # Обходим директорию рекурсивно
# for c in os.walk(start_dir):
#
#     print(c)

# res = int(input('fvfbgb: '))
# print(res)
# print((type(res)))

# lst2 = [1, "abc", -5, 7.68, True]
#
# res = filter(lambda x: type(x) in (int, float), lst2)
# print(list(res))

# a = 123
# res = getattr(a, '__mul__')(2)
# print(res)

# lst1 = ['связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях']
# def lst(*args):
#     st = [*args]
#     print(st)
#
# lst('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях')

# lst = [True, True, False]
# print(lst.count(True))
# print(sum(lst))
# print(True + False)

# d = {'r': '45', 'd': '56'}
# res = d.items()
# print(res)
# for i, v in enumerate(d.values()):
#     print(i, v)


# class Vectir:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# v1 = Vectir(1,2)
# print(type(v1.__dict__))