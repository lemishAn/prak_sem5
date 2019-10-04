'''
task2, program 4.2
Graph implemented as an adjacent matrix
Function route_min finds minimum path from NodeStart to NodeEnd 
'''
class Graph:
    def __init__(self, tmp):
        self.number_of_nodes = max(max(start, end) for start, end, weight in tmp) + 1
        INF = 10 ** 9
        self.matrix = [[INF]*self.number_of_nodes for i in range(self.number_of_nodes)]
        i = 0
        while i < len(tmp):
            self.matrix[tmp[i][0]][tmp[i][1]] = self.matrix[tmp[i][1]][tmp[i][0]] = tmp[i][2]
            i += 1

    def matrix_min(self, start):
        INF = 10 ** 9
        F = [INF] * self.number_of_nodes
        F[start] = 0
        for k in range(1, self.number_of_nodes):
            for i in range(self.number_of_nodes):
                for j in range(self.number_of_nodes):
                    if F[j] + self.matrix[j][i] < F[i]:
                        F[i] = F[j] + self.matrix[j][i]
        return F

    def route_min(self, NodeStart, NodeEnd):
        F = self.matrix_min(NodeStart)
        return F[NodeEnd]

A = input('Enter graph: ')
B = []
curr = 0
j = -1
for i in range(1, len(A) - 1):
    if A[i] == '[':
        B.append([])
        j += 1
        continue
    if A[i] in ' ,':
        B[j].append(curr)
        curr = 0
        continue
    if A[i] in '0123456789':
        curr = curr * 10 + int(A[i]) 
    if A[i] == ']':
        continue       
B[j].append(curr)
G = Graph(B)
NodeStart = int(input('Enter node one: '))
NodeEnd = int(input('Enter node two: '))
print(G.route_min(NodeStart, NodeEnd))
