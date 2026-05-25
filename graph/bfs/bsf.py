from collections import deque
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
            
    def bfs(self, src):
        visited = [False] * self.vertex
        queue = deque([src])        
        visited[src] = True  
        
        while queue:
            v = queue.popleft()
            print(v, end="->")
            
            for i in range(self.vertex):
                if self.mat[v][i] == 1 and visited[i] ==False:        
                    queue.append(i)
                    visited[i] = True   



g = Graph(6)
g.add_Edge(0,1)
g.add_Edge(0,2)
g.add_Edge(2,3)    
g.add_Edge(3,5)  
g.add_Edge(5,4)  
g.add_Edge(2,4)  



# g.print_Graph()
g.bfs(0)