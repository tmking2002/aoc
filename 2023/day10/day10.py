file = open('day10/input.txt', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

pipe_map = [list(row) for row in lines]

# Part 1

# search for S

connections = {'|': ['N', 'S'], '-': ['E', 'W'], 'L': ['N', 'E'], 'J': ['N', 'W'], 'F': ['S', 'E'], '7': ['S', 'W'], 'S': ['N', 'S', 'E', 'W'], '.': []}

for row in range(len(pipe_map)):
    for col in range(len(pipe_map[row])):
        if pipe_map[row][col] == 'S':
            start = (row, col)

def find_possible_next(start_loc, prev_loc):

    row, col = start_loc
    start_type = pipe_map[row][col]
    possible_next = []

    start_connections = connections[start_type]

    if 'N' in start_connections:
        if 'S' in connections[pipe_map[row-1][col]]:
            possible_next.append((row-1, col))

    if 'S' in start_connections:
        if 'N' in connections[pipe_map[row+1][col]]:
            possible_next.append((row+1, col))

    if 'E' in start_connections:
        if 'W' in connections[pipe_map[row][col+1]]:
            possible_next.append((row, col+1))

    if 'W' in start_connections:
        if 'E' in connections[pipe_map[row][col-1]]:
            possible_next.append((row, col-1))

    if prev_loc is not None:
        possible_next = [tup for tup in possible_next if tup != prev_loc]

    return possible_next

path = [start]

iteration = 0
prev_loc = None


while True:
    next_pipes = find_possible_next(start, prev_loc)

    if len(next_pipes) == 0 or (iteration > 1 and pipe_map[next_pipes[0][0]][next_pipes[0][1]] == 'S'):
        break
    else:
        path.append(next_pipes[0])
        prev_loc = start
        start = next_pipes[0]

    iteration += 1

print(len(path) / 2)

# Part 2

new_pipe_map = pipe_map

for row in range(len(pipe_map)):
    for col in range(len(pipe_map[row])):
        if (row, col) not in path:
            new_pipe_map[row][col] = '#'

def is_connected(row1, col1, row2, col2):
    if row1 >= len(pipe_map) or row2 >= len(pipe_map) or col1 >= len(pipe_map[0]) or col2 >= len(pipe_map[0]):
        return False

    type1 = pipe_map[row1][col1]
    type2 = pipe_map[row2][col2]

    if type1 == '#' or type2 == '#':
        return False

    if row1 == row2:
        if col1 == col2 + 1 and 'W' in connections[type1] and 'E' in connections[type2]:
            return True
        elif col1 == col2 - 1 and 'E' in connections[type1] and 'W' in connections[type2]:
            return True
    elif col1 == col2:
        if row1 == row2 + 1 and 'N' in connections[type1] and 'S' in connections[type2]:
            return True
        elif row1 == row2 - 1 and 'S' in connections[type1] and 'N' in connections[type2]:
            return True
    return False

big_map = []

for row in range(len(new_pipe_map) * 2):
    big_map.append([])
    for col in range(len(new_pipe_map[0]) * 2):
        if row % 2 == 0 and col % 2 == 0:
            big_map[row].append(new_pipe_map[int(row / 2)][int(col / 2)])
        else:
            if col % 2 == 1 and is_connected(int((row - 1) / 2), int((col - 1) / 2), int((row + 1) / 2), int((col - 1) / 2)):  # check if pipe is connected on left
                big_map[row].append('|')
            elif row % 2 == 1 and is_connected(int((row - 1) / 2), int((col - 1) / 2), int((row - 1) / 2), int((col + 1) / 2)):  # check if pipe is connected on top
                big_map[row].append('-')
            else:
                big_map[row].append('#')

for row in big_map:
    print(''.join(row))

print('\n')

def flood_fill(start_x, start_y):
    queue = [(start_x, start_y)]

    while queue:
        loc = queue.pop()

        posX = loc[0]
        posY = loc[1]

        if posY > 0:
            if big_map[posX][posY - 1] == '#':
                big_map[posX][posY - 1] = 'O'
                queue.append((posX, posY - 1))
        
        if posY < len(big_map[0]) - 1:
            if big_map[posX][posY + 1] == '#':
                big_map[posX][posY + 1] = 'O'
                queue.append((posX, posY + 1))

        if posX > 0:
            if big_map[posX - 1][posY] == '#':
                big_map[posX - 1][posY] = 'O'
                queue.append((posX - 1, posY))
        
        if posX < len(big_map) - 1:
            if big_map[posX + 1][posY] == '#':
                big_map[posX + 1][posY] = 'O'
                queue.append((posX + 1, posY))

for col in range(len(big_map[0])):
    flood_fill(0, col)
    flood_fill(len(big_map) - 1, col)

for row in range(len(big_map)):
    flood_fill(row, 0)
    flood_fill(row, len(big_map[0]) - 1)

inside = 0
inside_coords = []

for row in range(len(big_map)):
    for col in range(len(big_map[row])):
        if big_map[row][col] == '#':
            if row % 2 == 0 and col % 2 == 0:
                big_map[row][col] = 'I'
                inside += 1
                inside_coords.append((row, col))
            else: 
                big_map[row][col] = ' '

RED = '\033[91m'
RESET = '\033[0m'


for row in big_map:
    for col in row:
        if col == 'I':
            print(RED + col + RESET, end='')
        else:
            print(col, end='')
    print()

print('\n')

inside_coords = [(row / 2, col / 2) for row, col in inside_coords]

for row in range(len(new_pipe_map)):
    for col in range(len(new_pipe_map[row])):
        if (row, col) in path:
            print(new_pipe_map[row][col], end='')
        elif (row, col) in inside_coords:
            print(RED + 'I' + RESET, end='')
        else:
            print(new_pipe_map[row][col], end='')
    print()

print(inside)

row = 8
col = 7

print(new_pipe_map[int((row - 1) / 2)][int((col - 1) / 2)])
print(new_pipe_map[int((row + 1) / 2)][int((col - 1) / 2)])

print(is_connected(int((row - 1) / 2), int((col - 1) / 2), int((row + 1) / 2), int((col - 1) / 2)))
