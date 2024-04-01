import random as rnd

def gprint(grid):
    for row in grid:
        print(row)

# define cleaned cells
def cleaned(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                return True
            else:
                return False

def vacuum():
    # grid initialization
    grid = [[rnd.choice([0, 1]) for x in range(4)] for y in range(4)]
    # vacuum position initialization
    x, y = rnd.randint(0, 3), rnd.randint(0, 3)
    # vacuum movement
    movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    gprint(grid)
    print("Vacuum Position:", (x, y))
    # check for dirty grids
    while not cleaned(grid):
        for x in range(4):
            for y in range(4):
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    print("Cleaned:", (x, y))
                    gprint(grid)

        dx, dy = rnd.choice(movement)
        nx, ny = dx + x, dy + y
        # keeps new x,y within parameters
        if 0 <= nx < 4 and 0 <= ny < 4:
            x, y = nx, ny
            print("Moved:", (x, y))

vacuum()

# expected output (random trial):
# [1, 0, 1, 0]
# [0, 0, 0, 0]
# [1, 1, 1, 0]
# [0, 1, 0, 1]
# Vacuum Position: (1, 1)
# Cleaned: (0, 0)
# [0, 0, 1, 0]
# [0, 0, 0, 0]
# [1, 1, 1, 0]
# [0, 1, 0, 1]
# Cleaned: (0, 2)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [1, 1, 1, 0]
# [0, 1, 0, 1]
# Cleaned: (2, 0)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 1, 1, 0]
# [0, 1, 0, 1]
# Cleaned: (2, 1)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 1, 0]
# [0, 1, 0, 1]
# Cleaned: (2, 2)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 1, 0, 1]
# Cleaned: (3, 1)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 1]
# Cleaned: (3, 3)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]




