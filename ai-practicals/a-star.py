from simpleai.search import SearchProblem, astar


GOAL = 'HELLO WORLD'


class HelloProblem(SearchProblem):
 def actions(self, state):
# Return possible actions if the current state is less than the goal length
  if len(state) < len(GOAL):
   return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  else:
   return []


 def result(self, state, action):
# Append the action to the current state to form the new state
  return state + action
 def is_goal(self, state):
# Check if the current state matches the goal state
  return state == GOAL
 def heuristic(self, state):
# Calculate heuristic: number of wrong characters and missing characters
  wrong = sum([1 if state[i] != GOAL[i] else 0
   for i in range(len(state))])
  missing = len(GOAL) - len(state)
  return wrong + missing
# Initialize the problem with an empty initial state
problem = HelloProblem(initial_state='')
# Use A* to find the solution
result = astar(problem)
# Print the final state and the path of actions to reach it
print("Final State:", result.state)
print("Path to Solution:", result.path())
