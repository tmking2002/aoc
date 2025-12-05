test = False

if test == True:
    input_path = 'day4/sample.txt'
else:
    input_path = 'day4/input.txt'

with open(input_path) as f:
    data = f.read()
    lines = data.split('\n')

def mark_rolls(lines):

    rolls = []

    for y, row in enumerate(lines):
        for x, val in enumerate(list(row)):
            if val == '@':
                rolls.append((x, y))

    return rolls

def check_reachable(roll, rolls):
    
    adjacent_count = 0

    for x_diff in range(-1, 2):
        for y_diff in range(-1, 2):
            if ((roll[0] + x_diff, roll[1] + y_diff) in rolls) & (x_diff != 0 or y_diff != 0):
                adjacent_count += 1
                if adjacent_count == 4:
                    return False
                
    return True

rolls = mark_rolls(lines)

reachable_count = 0
reachable_dict = {}

for roll in rolls:
    reachable = check_reachable(roll, rolls)
    reachable_dict[roll] = reachable
    reachable_count += reachable

# print(reachable_dict)
print(reachable_count)
