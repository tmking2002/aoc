import re

file = open("day3/input.txt", "r")
lines = file.readlines()

# Part 1

numbers = [(int(num), index) for index, line in enumerate(lines) for num in re.findall(r'\d+', line)]
part_numbers = []

def check_for_symbol(number, row_num, first_column):
    last_column = first_column + len(str(number)) - 1

    # Search for symbol above 
    row_search = row_num - 1
    if row_search >= 0:
        row = lines[row_search]
        for column in range(max(first_column - 1, 0), min(last_column + 2, len(row))):
            if not row[column].isdigit() and row[column] != '.' and not row[column].isspace():
                return True
    
    # Search for symbol below
    row_search = row_num + 1
    if row_search < len(lines):
        row = lines[row_search]
        for column in range(max(first_column - 1, 0), min(last_column + 2, len(row))):
            if not row[column].isdigit() and row[column] != '.' and not row[column].isspace():
                return True
    
    # Search for symbol left
    row_search = row_num
    column_search = first_column - 1
    if column_search >= 0:
        row = lines[row_search]
        if not row[column_search].isdigit() and row[column_search] != '.' and not row[column_search].isspace():
            return True
        
    # Search for symbol right
    row_search = row_num
    column_search = last_column + 1
    if column_search < len(lines[row_search]):
        row = lines[row_search]
        if not row[column_search].isdigit() and row[column_search] != '.' and not row[column_search].isspace() and row[column_search] != '\n':
            return True
        
    return False

for number, row_num in list(set(numbers)):
    line = lines[row_num]

    unique_numbers = [x for x in re.split(r'\D+', line) if x != '' and x != '\n']
    
    first_column = re.search(r'\b{}\b'.format(re.escape(str(number))), line).start()

    num_occurences = unique_numbers.count(str(number))

    for i in range(num_occurences):
        symbol_found = check_for_symbol(number, row_num, first_column)

        if symbol_found:
            part_numbers.append(number)

        first_column = line.find(str(number), first_column + 1)

print(sum(part_numbers))
#print(part_numbers)

# Part 2

number_locs = []

for row_num, line in enumerate(lines):
    
    numbers = re.findall(r'\d+', line)

    for number in numbers:
        first_column = re.search(r'\b{}\b'.format(re.escape(str(number))), line).start()
        last_column = first_column + len(str(number)) - 1

        number_locs.append((number, row_num, first_column, last_column))

star_positions = []

for row_num, line in enumerate(lines):
    for col_num, char in enumerate(line):
        if char == '*':
            star_positions.append((row_num, col_num))

gears = {}

for star_position in star_positions:
    adjacent_numbers = 0
    number_1 = None
    number_2 = None
    for number, row_num, first_column, last_column in number_locs:
        if abs(row_num - star_position[0]) <= 1 and (abs(first_column - star_position[1]) <= 1 or abs(last_column - star_position[1]) <= 1):
            adjacent_numbers += 1
            if number_1 == None:
                number_1 = number
            else: 
                number_2 = number
    if adjacent_numbers == 2:
        gears[star_position] = (number_1, number_2)

gear_ratio = 0

for star_position, (number_1, number_2) in gears.items():
    gear_ratio += int(number_1) * int(number_2)

print(gear_ratio)

