'''
task 2, program 1
'''
if __name__ == '__main__':
    LINE = input()
    i, j, number_substrings = 1, 0, 1
    S = LINE[0: i]
    while number_substrings*S != LINE:
        j = LINE.find(S, i)
        if j == - 1:
            break
        S = LINE[0: j]
        number_substrings = LINE.count(S)
        if i == j:
            i *= 2
        else: i = j
    if (number_substrings*S == LINE) or (number_substrings == 1):
        print(number_substrings)
    else: print('Error: Not an integer number of substrings')
