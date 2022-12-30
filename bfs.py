graph = {
'A' : ['B', 'C'],
'B' : ['A', 'D'],
'C' : ['A', 'D', 'E'],
'D' : ['B', 'C', 'E'],
'E' : ['C', 'D']
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue


def bfs(visited,graph,node):

    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m,end=" ")

        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')    # function calling