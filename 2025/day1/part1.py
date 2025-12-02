import operator

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
    distance = int(instruction.removeprefix(direction)) % 100

    new_pos = move_map[direction](pos, distance)

    if new_pos < 0:
        new_pos += 100
    elif new_pos > 99:
        new_pos -= 100

    return new_pos

pos = 50
zero_count = 0

for instruction in lines:
    pos = move_dial(pos, instruction)
    if pos == 0:
        zero_count += 1

print(zero_count)