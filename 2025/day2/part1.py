test = False

if test == True:
    input_path = 'day2/sample.txt'
else:
    input_path = 'day2/input.txt'

with open(input_path) as f:
    data = f.read()
    ranges = data.split(',')

def check_validity(number):

    number_str = str(number)

    if len(number_str) % 2 == 1:
        return True

    first_half = number_str[:int(len(number_str) / 2)]
    second_half = number_str[int(len(number_str) / 2):]

    if first_half == second_half:
        return False
    else:
        return True
    
def check_range(range_str):
    start, end = range_str.split('-')

    sum = 0

    for i in range(int(start), int(end) + 1):
        if check_validity(i) == False:
            sum += i

    return sum

def find_sum(ranges):

    sum = 0

    for range_str in ranges:
        sum += check_range(range_str)

    return sum

print(find_sum(ranges))