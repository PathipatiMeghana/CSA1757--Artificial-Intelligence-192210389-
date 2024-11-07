from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Queue to store nodes to explore

    while queue:
        node = queue.popleft()  # Pop the first node from the queue
        
        if node not in visited:
            print(node, end=" ")  # Visit and print the node
            visited.add(node)  # Mark the node as visited
            
            # Add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph (represented as an adjacency list)
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

# Perform BFS starting from node 1
bfs(graph, 1)