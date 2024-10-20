from __future__ import print_function
from simpleai.search import astar, SearchProblem


GOAL = '''1-2-3
4-5-6
7-8-e'''
print("Goal: ")
print(GOAL)

INITIAL = '''4-1-2
7-e-3
8-5-6'''
print("Initial: ")
print(INITIAL)


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string):
    return [row.split('-') for row in string.split('\n')]


def find_location(row, element):
    for i in range(len(row)):      
        for j in range(len(row[i])):
            if row[i][j] == element:
                return i, j




goal_positions = {
    number: find_location(string_to_list(GOAL), number)
    for number in '12345678e'
    }


class EightPuzzleProblem(SearchProblem):
    def actions(self, state):
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')
        actions = []
        if row_e > 0: actions.append(rows[row_e - 1][col_e])
        if row_e < 2: actions.append(rows[row_e + 1][col_e])
        if col_e > 0: actions.append(rows[row_e][col_e - 1])
        if col_e < 2: actions.append(rows[row_e][col_e + 1])
        return actions


    def result(self, state, action):
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')
        row_n, col_n = find_location(rows, action)
        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]
        return list_to_string(rows)


    def is_goal(self, state):
        return state == GOAL


    def cost(self, state1, action, state2):
        return 1


    def heuristic(self, state):
        rows = string_to_list(state)
        distance = 0
        for number in '12345678e':
            row_n, col_n = find_location(rows, number)
            row_n_goal, col_n_goal = goal_positions[number]
            distance += abs(row_n - row_n_goal) + abs(col_n - col_n_goal)
        return distance


result = astar(EightPuzzleProblem(INITIAL))


for action, state in result.path():
    print('Move number', action)
    print(state)
