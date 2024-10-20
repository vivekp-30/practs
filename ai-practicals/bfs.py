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
queue=[]
ans=[]
def bfs(node,graph,visited):
    queue=[node]
    visited.append(node)
    ans.append(node)
    level={}
    level[node]=0
    while queue:
        curNode=queue.pop(0)
        for child in graph[curNode]:
            if child not in visited:
                ans.append(child)
                queue.append(child)
                visited.append(node)
                level[child]=level[curNode]+1
                print(level)
   






print(bfs('A',graph,visited))
print(ans)
