graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

# Implement BFS Logic
def bfs(start):
    queue = [start]
    levels = {}  # Keeps track of levels
    levels[start] = 0  # Depth of start node is 0
    visited = set([start])
    
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        
        for neighbor in neighbours:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                levels[neighbor] = levels[node] + 1
    
    print(levels)  # Print graph levels as they are updated
    return visited

print(bfs('A'))  # Print visited nodes

# For finding BFS paths
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]  # Queue stores (vertex, path)
    
    while queue:
        (vertex, path) = queue.pop(0)
        
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]  # Return the full path to goal
            else:
                queue.append((next, path + [next]))

result = list(bfs_paths(graph, 'A', 'F'))
print(result)

# For finding the shortest path using BFS
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))  # Get the first path from generator
    except StopIteration:
        return None

result1 = shortest_path(graph, 'A', 'F')
print(result1)
