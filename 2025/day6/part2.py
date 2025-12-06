import math
import re

test = False

if test == True:
    input_path = 'day6/sample.txt'
else:
    input_path = 'day6/input.txt'

with open(input_path) as f:
    data = f.read()
    lines = data.split('\n')

def get_operations(lines):
    # take full lines (list) and return dictionary of operations and 
    # which cols they apply to
    operations_list = []
    
    operations = list(re.finditer(r'[+*]', lines[-1:][0]))
    
    for i, operation in enumerate(operations):
        if i == (len(operations) - 1):
            operations_list.append([operation.group(), (operation.start(), len(lines[0]))])
        else:
            operations_list.append([operation.group(), (operation.start(), operations[i+1].start() - 2)])

    return operations_list

def reverse_operands(cur_operands_reversed):
    # takes a single list of operands the wrong way and reverses it
    # e.g. input: ['123', ' 45', '  6'], output: [1, 24, 356]
    length = len(cur_operands_reversed[0])
    cur_operands = []

    for i in range(length):
        cur_num_str = ''.join([num[i] for num in cur_operands_reversed])

        if cur_num_str.strip() != '':
            cur_num = int(cur_num_str)
        else: 
            cur_num = 0

        cur_operands.append(cur_num)
    
    return cur_operands

def get_operands(lines, operations_list):
    operands_reversed = []
    for _, loc in operations_list:
        start, end = loc[0], loc[1]
        cur_operands_reversed = []
        for line in lines[:-1]:
            cur_operand_reversed = line[start:(end+1)]
            cur_operands_reversed.append(cur_operand_reversed)
        operands_reversed.append(cur_operands_reversed)

    operands = []
    for cur_operands_reversed in operands_reversed:
        operands.append(reverse_operands(cur_operands_reversed))

    return operands

def compute_grand_total(operands, operations_list):
    operations = [x[0] for x in operations_list]
    grand_total = 0

    for i in range(len(operands)):
        if operations[i] == '+':
            grand_total += sum(operands[i])
        elif operations[i] == '*':
            grand_total += math.prod(operands[i])

    return grand_total

operations = get_operations(lines)
operands = get_operands(lines, operations)
grand_total = compute_grand_total(operands, operations)

# print(operations)
# print(operands)
print(grand_total)