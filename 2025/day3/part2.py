test = False

if test == True:
    input_path = 'day3/sample.txt'
else:
    input_path = 'day3/input.txt'

with open(input_path) as f:
    data = f.read()
    banks = data.split('\n')

def find_largest_number(remaining_bank, digits_left):
    # remaining_bank is a list
    # digits_left starts at 12 and goes down by one every time

    # return largest number in options and location of first occurrence
    options = remaining_bank[:(len(remaining_bank) - digits_left + 1)]
    print(options)
    
    largest = max(options)
    loc = options.index(largest)

    return largest, loc


def find_highest_joltage(bank, length=12):

    digits_left = 12
    joltage = ''
    
    bank = list(bank)

    for i in range(length):
        largest, loc = find_largest_number(bank, digits_left)
        print(largest, loc)
        bank = bank[(loc+1):]
        digits_left -= 1
        joltage = f'{joltage}{str(largest)}'

    return int(joltage)

sum = 0

for bank in banks:
    sum += find_highest_joltage(bank)

print(sum)