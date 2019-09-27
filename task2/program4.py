'''
task2, program 2
Graph implemented as an adjacent list
'''
class Graph:
    def __init__(self, tmp):
        self.res = []
        i = 0
        while i < len(tmp):
            while len(self.res) <= tmp[i][0]:
                self.res.append([])
            while len(self.res) <= tmp[i][1]:
                self.res.append([])
            self.res[tmp[i][0]].append(tmp[i][1])
            self.res[tmp[i][1]].append(tmp[i][0])
            i += 1
        self.bone = len(self.res)
        self.visited = [False] * self.bone
        self.level = [-1] * self.bone

    def dfs(self, v):
        self.visited[v] = True
        print(v)
        for w in self.res[v]:
            if not self.visited[w]:
                self.dfs(w)

    def bfs(self, s):
        self.level[s] = 0
        queue = [s]
        while queue:
            v = queue.pop(0)
            print(v)
            for w in self.res[v]:
                if self.level[w] is -1:
                    queue.append(w)
                    self.level[w] = self.level[v] + 1
