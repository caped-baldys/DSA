graph = {
'A' : ['B', 'C'],
'B' : ['A', 'D'],
'C' : ['A', 'D', 'E'],
'D' : ['B', 'C', 'E'],
'E' : ['C', 'D']
}

visited = set()

def dfs(visited,graph,root):
    if root not in visited:
        print(root,end='->')
        visited.add(root)
        for neighnour in graph[root]:
            dfs(visited,graph,neighnour)

dfs(visited,graph,'A')