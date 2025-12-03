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

    length = len(number_str)

    for substr_len in range(1, int(length / 2) + 1):
        if number_str.replace(number_str[:substr_len], '') == '':
            return False
        
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