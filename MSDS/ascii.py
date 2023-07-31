a = 'p'
print(ord(a))

a = 65
print(chr(a))

d = 'pt'
print(ord('p')*128+ord('t'))

print(2000/3)

lst_a = [[0, 1, 0, 1],
         [1, 0, 0, 0],
         [1, 0, 1, 1]]
lst_b= [1, 1, 1, 0]
and_list = [elt_a * elt_b for (elt_a, elt_b) in zip(lst_a, lst_b)]

# print(and_list)

import numpy as np
arr1 = np.array([[0, 1, 0, 1], [1, 0, 0, 0], [1, 0, 1, 1]] , dtype=bool)
arr2 = np.array([1, 1, 1, 0], dtype=bool)
res = np.dot(arr1 , arr2)
# print(res)

x = zip(lst_a, lst_b)
# print(tuple(x))

for elt_a , elt_b in zip(lst_a, lst_b):
    print(f'elt_a is {elt_a} and elt_b is {elt_b}')
    res = [elt_a*elt_b]
    print(res)

import random from random