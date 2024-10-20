capacity = (12, 8, 5)
x, y, z = capacity
memory = {}
ans = []


def get_all_states(state):
    a, b, c = state
    if a == 6 and b == 6:
        ans.append(state)
        return True
    if (a, b, c) in memory:
        return False
    memory[(a, b, c)] = True
    moves = [
        (a, b, x, y),
        (a, c, x, z),
        (b, a, y, x),
        (b, c, y, z),
        (c, a, z, x),
        (c, b, z, y)
    ]
    for source, dest, src_cap, dest_cap in moves:
        new_state = list(state)
        transfer_amount = min(source, dest_cap - dest)
        new_state[new_state.index(source)] -= transfer_amount
        new_state[new_state.index(dest)] += transfer_amount
        if get_all_states(tuple(new_state)):
            ans.append(state)
            return True
    return False


initial_state = (12, 0, 0)


print("Starting work...\n")
if get_all_states(initial_state):
    ans.reverse()
    for state in ans:
        print(state)
else:
    print("No solution found.")
