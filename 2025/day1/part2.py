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
    distance_adj = distance % 100

    new_pos = operation(pos, distance_adj)
    new_pos_adj = new_pos

    if new_pos < 0:
        new_pos_adj += 100
    elif new_pos > 99:
        new_pos_adj -= 100

    passed_0 = int(np.floor((new_pos_adj + distance - 1) / 100))

    if new_pos_adj == 0:
        passed_0 += 1
    if (pos == 0) & (passed_0 > 0) & (distance < 100):
        passed_0 -= 1
    
    return new_pos_adj, passed_0

def find_password(lines, verbose=False):

    pos = 50
    zero_count = 0

    for instruction in lines:
        new_pos, passed_0 = move_dial(pos, instruction)

        if verbose:
            print(f'{pos} {instruction} - {new_pos} {passed_0}')
        
        pos = new_pos
        zero_count += passed_0

    return zero_count

print(find_password(lines))