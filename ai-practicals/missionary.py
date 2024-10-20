from collections import deque


# Define the starting and goal states
start_state = (3, 3, 1)  # (missionaries on left, cannibals on left, boat on left)
goal_state = (0, 0, 0)  # (missionaries on left, cannibals on left, boat on left)


# Helper function to check if a state is valid (no missionaries eaten)
def is_valid_state(missionaries, cannibals):
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:
        return False
    if (3 - missionaries) > 0 and (3 - missionaries) < (3 - cannibals):
        return False
    return True


# Get all possible next states based on the current state
def get_successors(state):
    successors = []
    missionaries, cannibals, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Possible moves: (missionaries, cannibals)
   
    for move in moves:
        m, c = move
        if boat == 1:  # Boat is on the left bank
            new_state = (missionaries - m, cannibals - c, 0)  # Move to the right bank
        else:  # Boat is on the right bank
            new_state = (missionaries + m, cannibals + c, 1)  # Move to the left bank
       
        if is_valid_state(new_state[0], new_state[1]):
            successors.append(new_state)
   
    return successors


# Breadth-First Search (BFS) to find the solution
def bfs(start, goal):
    queue = deque([(start, [])])  # (current state, path to reach state)
    visited = set()
   
    while queue:
        current_state, path = queue.popleft()
       
        if current_state == goal:
            return path + [current_state]
       
        if current_state in visited:
            continue
       
        visited.add(current_state)
       
        for successor in get_successors(current_state):
            if successor not in visited:
                queue.append((successor, path + [current_state]))
   
    return None


# Solve the problem
solution = bfs(start_state, goal_state)


# Print the solution
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
