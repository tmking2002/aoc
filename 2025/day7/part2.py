import re
from functools import lru_cache

test = False

if test == True:
    input_path = 'day7/sample.txt'
else:
    input_path = 'day7/input.txt'

with open(input_path) as f:
    data = f.read()
    lines = data.split('\n')
    rows = len(lines)
    cols = len(lines[0])

def find_start(lines):
    return (re.search('S', lines[0]).start(), 0)

def find_splitters(lines):
    # return list of (x, y) tuples
    splitters = []
    for i, line in enumerate(lines):
        cur_splitters_match = list(re.finditer(r'[\^]', line))
        cur_splitters = [(match.start(), i) for match in cur_splitters_match]
        for loc in cur_splitters:
            splitters.append(loc)
    return splitters

@lru_cache
def simulate_single_movement(row, col):
    try:
        new_location = (row, col + 1)
        assert new_location not in splitters
        return [new_location]
    except:
        new_location_1 = (row - 1, col + 1)
        new_location_2 = (row + 1, col + 1)
        return [new_location_1, new_location_2]


def simulate_move(beam_dict):
    # beam_dict is dict with format (tuple): count
    new_beam_dict = {}

    for beam_location in beam_dict.keys():
        if beam_location[1] == rows:
            return beam_dict, True
        
        new_location_list = simulate_single_movement(beam_location[0], beam_location[1])

        for location in new_location_list:
            if location in new_beam_dict:
                new_beam_dict[location] += beam_dict[beam_location]
            else:
                new_beam_dict[location] = beam_dict[beam_location]           

    return new_beam_dict, False

def display(beam_list, splitters):
    str = ''
    start = beam_list[0][0]
    all_locations_flat = []
    for beam in beam_list:
        all_locations_flat.extend(beam)

    for col in range(rows):
        for row in range(cols):
            if (row, col) == start:
                str += 'S'
            elif (row, col) in all_locations_flat:
                str += '|'
            elif (row, col) in splitters:
                str += '^'
            else:
                str += '.'
        str += '\n'
    
    return str

start = find_start(lines)
beam_dict = {start: 1}

splitters = find_splitters(lines)
cur_row = 0

while True:
    print(cur_row)
    beam_dict, finished = simulate_move(beam_dict)
    if finished:
        break
    cur_row += 1

print(sum(beam_dict.values()))