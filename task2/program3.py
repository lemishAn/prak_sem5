'''
task 2, program 3
'''
from itertools import product

my_dict = {'0': ' ',
           '1': '',
           '2': ('a', 'b', 'c'),
           '3': ('d', 'e', 'f'),
           '4': ('g', 'h', 'i'),
           '5': ('j', 'k', 'l'),
           '6': ('m', 'n', 'o'),
           '7': ('p', 'q', 'r'),
           '8': ('s', 't', 'v'),
           '9': ('w', 'x', 'y', 'z')}
S = input()
A = []
for i in S:
    if i == '1':
        continue
    A.append(my_dict[i])
LST = list(product(*A))
LST2 = []
for i in range(len(LST)):
    LST2.append(''.join((LST[i])))
print(LST2)
