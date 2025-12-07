import re

test = True

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

def simulate_move(beam_list, splitters, rows, cur_row):
    # beam_list is list of list of tuples
    # last tuple in each list is current location
    splits = 0

    current_locations = [(i, beam[-1]) for i, beam in enumerate(beam_list)]
    all_locations_flat = []
    for beam in beam_list:
        all_locations_flat.extend(beam)

    for beam_num, beam_location in reversed(current_locations):
        if beam_location[1] == rows:
            return beam_list, splits, True
        
        if beam_location[1] != cur_row:
            beam_list.pop(beam_num)
            continue

        try:
            new_location = (beam_location[0], beam_location[1] + 1)
            assert new_location not in splitters
            if new_location not in all_locations_flat:
                beam_list[beam_num].append(new_location)
                all_locations_flat.append(new_location)
        except:
            splits += 1
            new_location_1 = (beam_location[0] - 1, beam_location[1] + 1)
            new_location_2 = (beam_location[0] + 1, beam_location[1] + 1)

            if new_location_1 not in all_locations_flat:
                beam_list[beam_num].append(new_location_1)
                all_locations_flat.append(new_location_1)
                
            if new_location_2 not in all_locations_flat:
                beam_list.insert(beam_num+1, [new_location_2])
                all_locations_flat.append(new_location_2)

    return beam_list, splits, False

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

beam_list = [[find_start(lines)]]

splitters = find_splitters(lines)
total_splits = 0
cur_row = 0

while True:
# for _ in range(5):
    beam_list, splits, finished = simulate_move(beam_list, splitters, rows, cur_row)
    total_splits += splits
    # for beam in beam_list:
    #     print(beam)
    # print(beam_list)
    # print(display(beam_list, splitters))
    # print(splits)
    # print()
    # print()
    if finished:
        break
    cur_row += 1

# with open('day7/display.txt', 'w') as f:
#     f.write(display(beam_list, splitters))

print(total_splits)