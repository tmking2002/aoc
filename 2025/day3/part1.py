test = False

if test == True:
    input_path = 'day3/sample.txt'
else:
    input_path = 'day3/input.txt'

with open(input_path) as f:
    data = f.read()
    banks = data.split('\n')

def find_highest_joltage(bank):
    number_list = list(bank)

    highest = max(number_list)

    remaining = number_list[(number_list.index(highest) + 1):]

    if len(remaining) == 0:
        adjusted_list = number_list.copy()
        adjusted_list.remove(highest)
        highest = max(adjusted_list)

    number_list = number_list[(number_list.index(highest) + 1):]

    second_highest = max(number_list)

    return int(highest + second_highest)

sum = 0

for bank in banks:
    sum += find_highest_joltage(bank)

print(sum)