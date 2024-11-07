from collections import deque

# Initial state
start_state = (3, 3, 0)  # (missionaries_left, cannibals_left, boat_position)
goal_state = (0, 0, 1)

# Allowed moves (missionaries, cannibals)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

# Function to check if state is valid
def is_valid_state(missionaries, cannibals):
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if (missionaries > 0 and missionaries < cannibals) or (3 - missionaries > 0 and 3 - missionaries < 3 - cannibals):
        return False
    return True

# BFS to find solution
def solve_missionaries_and_cannibals():
    queue = deque([(start_state, [])])  # (state, path)
    visited = set()

    while queue:
        (missionaries, cannibals, boat_position), path = queue.popleft()

        if (missionaries, cannibals, boat_position) in visited:
            continue
        visited.add((missionaries, cannibals, boat_position))

        if (missionaries, cannibals, boat_position) == goal_state:
            return path + [(missionaries, cannibals, boat_position)]

        for m, c in moves:
            if boat_position == 0:
                new_state = (missionaries - m, cannibals - c, 1)
            else:
                new_state = (missionaries + m, cannibals + c, 0)

            if is_valid_state(*new_state[:2]):
                queue.append((new_state, path + [(missionaries, cannibals, boat_position)]))

    return "No solution found"

# Print solution steps
solution = solve_missionaries_and_cannibals()
if solution != "No solution found":
    for i, state in enumerate(solution):
        print(f"Step {i+1}: Missionaries = {state[0]}, Cannibals = {state[1]}, Boat Position = {'Right' if state[2] else 'Left'}")
else:
    print(solution)