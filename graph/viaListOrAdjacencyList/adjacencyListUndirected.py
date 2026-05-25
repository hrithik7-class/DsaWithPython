class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex]= []
            
    def add_edge(self, src ,dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)
        
    def print_graph(self):
        for v in self.adjacency_list:
            print(v, "->", self.adjacency_list[v])                    
            
            
            
g = Graph()

g.add_edge(1,2)
g.add_edge(2,3)

g.add_edge(2,4)

g.add_edge(1,4)

g.add_edge(3,4)

g.add_edge(4,5)

g.add_edge(3,5)


g.print_graph()            
            