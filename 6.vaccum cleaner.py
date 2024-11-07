# Define the room with dirty spots (1 = dirty, 0 = clean)
room = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0]
]

# Vacuum cleaner starts at position (0, 0)
vacuum_pos = [0, 0]

# Function to clean the room
def clean_room():
    global vacuum_pos
    total_cleaned = 0

    # Keep cleaning until all spots are clean
    while total_cleaned < sum(sum(row) for row in room):  # Check if any spot is dirty
        x, y = vacuum_pos
        if room[x][y] == 1:  # If the spot is dirty, clean it
            room[x][y] = 0  # Clean the spot
            total_cleaned += 1
            print(f"Cleaned position: ({x}, {y})")

        # Move to next position (simulating random movement)
        # Here we are just moving right until we hit the end of the row, then move down
        if y + 1 < len(room[0]):
            vacuum_pos = [x, y + 1]  # Move right
        elif x + 1 < len(room):
            vacuum_pos = [x + 1, 0]  # Move to next row (start from left)
        else:
            break  # If we're at the end of the room, stop cleaning

    print("Room cleaned successfully!")

# Print initial state of the room
print("Initial Room:")
for row in room:
    print(row)

# Start cleaning
clean_room()

# Print final state of the room
print("\nFinal Room after cleaning:")
for row in room:
    print(row)