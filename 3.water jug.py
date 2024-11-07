from collections import deque

# Initialize jug capacities and target
JUG_A_CAPACITY = 4
JUG_B_CAPACITY = 3
TARGET = 2

# BFS to find solution
def water_jug():
    visited = set()  # Track visited states to avoid loops
    queue = deque([(0, 0)])  # Start with both jugs empty
    steps = []  # To record the steps

    while queue:
        a, b = queue.popleft()
        
        # Check if we've reached the target
        if a == TARGET or b == TARGET:
            steps.append((a, b))
            return steps
        
        # If state has already been visited, skip it
        if (a, b) in visited:
            continue
        
        visited.add((a, b))
        steps.append((a, b))

        # Possible moves
        queue.extend([
            (JUG_A_CAPACITY, b),  # Fill Jug A
            (a, JUG_B_CAPACITY),  # Fill Jug B
            (0, b),               # Empty Jug A
            (a, 0),               # Empty Jug B
            (min(a + b, JUG_A_CAPACITY), b - (min(a + b, JUG_A_CAPACITY) - a)),  # Pour B -> A
            (a - (min(a + b, JUG_B_CAPACITY) - b), min(a + b, JUG_B_CAPACITY))   # Pour A -> B
        ])
    
    return "No solution"

# Find and print steps
solution = water_jug()
for step in solution:
    print(f"Jug A: {step[0]}L, Jug B: {step[1]}L")