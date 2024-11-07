import heapq

# Define the goal state
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # 0 is the empty space

# Calculate Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(target_x - i) + abs(target_y - j)
    return distance

# Find the possible moves for the empty space (0)
def get_neighbors(state):
    neighbors = []
    x, y = [(ix, iy) for ix, row in enumerate(state) for iy, val in enumerate(row) if val == 0][0]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Algorithm
def a_star(start):
    queue = []
    heapq.heappush(queue, (0 + manhattan_distance(start), start, []))
    visited = set()

    while queue:
        _, current, path = heapq.heappop(queue)
        if current == GOAL_STATE:
            return path

        visited.add(tuple(tuple(row) for row in current))

        for neighbor in get_neighbors(current):
            if tuple(tuple(row) for row in neighbor) not in visited:
                new_path = path + [neighbor]
                heapq.heappush(queue, (len(new_path) + manhattan_distance(neighbor), neighbor, new_path))

# Example Input
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

# Solve and print moves
solution = a_star(initial_state)
print("Solution:")
for step in solution:
    for row in step:
        print(row)
    print()