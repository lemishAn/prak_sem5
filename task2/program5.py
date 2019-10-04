'''
task 2, program 5
Graph implemented as an adjacent matrix
'''
class Graph:
    def __init__(self, tmp, number_of_nodes):
        INF = 10 ** 9
        self.matrix = [[INF]*number_of_nodes for i in range(number_of_nodes)]
        i = 0
        while i < len(tmp):
            self.matrix[tmp[i][0] - 1][tmp[i][1] - 1] = tmp[i][2]
            i += 1

    def matrix_min(self, start, number_of_nodes):
        INF = 10 ** 9
        F = [INF] * number_of_nodes
        F[start] = 0
        for k in range(1, number_of_nodes):
            for i in range(number_of_nodes):
                for j in range(number_of_nodes):
                    if F[j] + self.matrix[j][i] < F[i]:
                        F[i] = F[j] + self.matrix[j][i]
        return F

A = input('Enter graph: ')
N = int(input('Enter N: '))
X = int(input('Start node: '))
TIMES = []
j = -1
curr = 0
for i in range(1, len(A) - 1):
    if A[i] == "[":
        TIMES.append([])
        j += 1
        continue
    if A[i] in ' ,':
        TIMES[j].append(curr)
        curr = 0
        continue
    if A[i] in '0123456789':
        curr = curr * 10 + int(A[i]) 
    if A[i] == ']':
        continue
TIMES[j].append(curr)
G = Graph(TIMES, N)
MAX_ROUTE = max(G.matrix_min(X - 1, N))
if MAX_ROUTE != 10 ** 9:
    print(MAX_ROUTE)
else: print(-1)
