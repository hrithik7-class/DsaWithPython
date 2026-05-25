class Graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.mat = [[0]*vertex for _ in range(vertex)]
        
    def add_Edge(self, src ,dest):
        self.mat[src][dest] = 1
        self.mat[dest][src] = 1
        
    # def print_Graph(self):
    #     for row in self.mat:
    #         print(" ".join(map(str, row)))
            
    def dfs(self, src):
        visited = [False] * self.vertex
        stack = [src]
        
        while stack:
            v = stack.pop()

            if (visited[v] == False):
                print(v, end="->")
                visited[v] = True

            for i in range(self.vertex):
                if self.mat[v][i] == 1 and not visited[i]:
                    stack.append(i)


g = Graph(6)
g.add_Edge(0,1)
g.add_Edge(0,2)
g.add_Edge(2,3)    
g.add_Edge(3,5)  
g.add_Edge(5,4)  
g.add_Edge(2,4)  



# g.print_Graph()
g.dfs(0)