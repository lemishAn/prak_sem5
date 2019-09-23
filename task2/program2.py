'''
task 2, program 2
'''
TEXT, S = ' ', ' '
while S:
    S = input()
    if S:
        TEXT = TEXT + S + ' '
LST = TEXT.split()
#print(LST)
my_dict = {}
for i in LST:
    k = my_dict.setdefault(i, 0)
    my_dict[i] += 1
max_value = 0
#print(len(my_dict))
for i in my_dict:
    #print(i)
    if my_dict[i] > max_value:
        max_value = my_dict[i]
        word = i
    elif my_dict[i] == max_value:
        word = '-'
print(word)
