import operator
import numpy as np

test = False

if test == True:
    input_path = 'day1/sample.txt'
else:
    input_path = 'day1/input.txt'

with open(input_path) as f:
    data = f.read()
    lines = data.split('\n')

move_map = {"L": operator.sub, "R": operator.add}

def move_dial(pos, instruction):
    direction = instruction[0]
    operation = move_map[direction]

    distance = int(instruction.removeprefix(direction))
    full_rotations = np.floor(distance / 100)
    distance_adj = distance % 100

    new_pos = operation(pos, distance_adj)
    new_pos_adj = new_pos

    clicks = full_rotations

    if new_pos < 0:
        new_pos_adj += 100
        clicks += 1
    elif new_pos > 99:
        new_pos_adj -= 100
        clicks += 1
    elif new_pos_adj == 0:
        clicks += 1

    print(pos == 0)
    
    if (pos == 0) and (new_pos < 0 or new_pos > 99 or new_pos_adj == 0):
        clicks -= 1

    return new_pos_adj, clicks

def find_password(lines, verbose=False):

    pos = 50
    click_count = 0

    for instruction in lines:
        new_pos, clicks = move_dial(pos, instruction)

        if verbose:
            print(f'{pos} {instruction} - {new_pos} {clicks}')
        
        pos = new_pos
        click_count += clicks

    return click_count

# print(find_password(lines))