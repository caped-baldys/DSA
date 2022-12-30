

class Graph():

    def __init__(self,Node):
        self.node = Node
        self.adj_list = {}

        for node1 in self.node:
            self.adj_list[node1] = []


    def add_edge(self,u,v):
        self.adj_list[v].append(u)
        self.adj_list[u].append(v)


    def degree(self,u):
        deg = len(self.adj_list[u])
        return deg

    def print_adj_list(self):
        for node in self.node:
            print(node,'=',self.adj_list[node])


nodes_1= ["A","B","C","D","E"]
edges = [("A",'B'),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")]

graph = Graph(nodes_1)

for edge in edges:
    u,v = edge
    graph.add_edge(u, v)
graph.print_adj_list()

print('Degree of node A',graph.degree("A"))
