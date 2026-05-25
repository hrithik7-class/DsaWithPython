class Graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.mat = [[0]*vertex for _ in range(vertex)]
        
    def add_Edge(self, src ,dest):
        self.mat[src][dest] = 1
        self.mat[dest][src] = 1
        
    def print_Graph(self):
        for row in self.mat:
            print(" ".join(map(str, row)))
            
            
            
g = Graph(5)
g.add_Edge(0,1)
g.add_Edge(0,2)
g.add_Edge(1,3)    


g.print_Graph()
             
                    
                    
                    