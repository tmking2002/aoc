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

def iteration(rolls, iter):

    print(f'Iteration {iter}')

    reachable_count = 0
    reachable_dict = {}

    removal_list = []

    for roll in rolls:
        reachable = check_reachable(roll, rolls)
        reachable_dict[roll] = reachable
        reachable_count += reachable
        if reachable:
            removal_list.append(roll)
    
    removals = len(removal_list)

    for roll in removal_list:
        rolls.remove(roll)

    return removals, rolls, reachable_count

rolls = mark_rolls(lines)
removals = 1
final_reachable = 0
iter = 1

while removals > 0:
    removals, rolls, reachable_count = iteration(rolls, iter)
    final_reachable += reachable_count
    iter += 1

print(final_reachable)