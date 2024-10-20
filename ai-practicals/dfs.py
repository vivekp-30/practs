graph = {
    'A': set(['B', 'C']),
    'B': set(['D', 'E']),
    'C': set(['F', 'G']),
    'D': set(),  
    'E': set(),
    'F': set(),
    'G': set(),
}
visited=[]
ans=[]
def dfs(node,graph,visited):
    visited.append(node)
    ans.append(node)
    for child in graph[node]:
        if child not in visited:
            dfs(child,graph,visited)


dfs('A',graph,visited)
print(ans)
