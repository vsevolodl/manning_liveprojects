# Manning Live Project
# Python Fundamentals Variables
#
# Milestone 1
#
# int, float, str, list, tuple, and dict.

a: int = 6
b: int = a
a: int = 5
print(a, b)

c: float = 1.5
d: float = c
c: float = 2.5
print(c, d)

e: str = 'one'
f: str = e
e: str = 'two'
print(e, f)

list_a: list = [1, 2, 3]
list_b: list = list_a
list_a: list = [4, 5, 6]
print(list_a, list_b)

list_c: list = [11, 12, 13]
list_d: list = list_c
list_c[1] = 99
print(list_c, list_d)

tuple_a: tuple = (1, 2, 3)
tuple_b: tuple = tuple_a
tuple_a: tuple = (4, 5, 6)
print(tuple_a, tuple_b)

# next block of code should result in error and it does :)
# tuple_c: tuple = (1, 2, 3)
# tuple_d: tuple = tuple_c
# tuple_c[1] = 9
# print(tuple_a, tuple_b)

dict_a: dict = {1: 'one', 2: 'two', 3: 'three'}
dict_b: dict = dict_a
dict_a: dict = {1: 'four', 2: 'five', 3: 'six'}
print(dict_a, dict_b)

dict_a: dict = {1: 'one', 2: 'two', 3: 'three'}
dict_b: dict = dict_a
dict_b[2] = 'ninety nine'
print(dict_a, dict_b)
