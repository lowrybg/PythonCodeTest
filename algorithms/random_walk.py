import random


def random_walk_2d(steps):
    # Simulates a 2D random walk on a grid.
    # Returns the path taken as a list of (x, y) coordinates.
    x, y = 0, 0
    path = [(x, y)]

    for _ in range(steps):
        direction = random.choice(['N', 'S', 'E', 'W'])

        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1

        path.append((x, y))

    return path


# Simulate 10 steps of a random walk
walk_path = random_walk_2d(10)
print("Path taken:", walk_path)
print("Final position:", walk_path[-1])