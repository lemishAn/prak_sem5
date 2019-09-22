'''
task 2, program 1
'''
if __name__ == '__main__':
    line = input()
    i, j, number_substrings = 1, 0, 1
    s = line[0: i]
    while number_substrings*s != line:
        j = line.find(s, i)
        if j == - 1:
            break
        s = line[0: j]
        number_substrings = line.count(s)
        if i == j:
            i *= 2
        else: i = j
    if (number_substrings*s == line) or (number_substrings == 1):
        print(number_substrings)
    else: print('Error: Not an integer number of substrings')
