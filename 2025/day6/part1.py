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

def get_operands(lines):
    # take full lines (list) and return list of lists
    operands_reversed = []

    for i, line in enumerate(lines):
        if i == (len(lines) - 1):
            operations = re.findall(r'[+*]', line)
        else:
            cur_operands_raw = line.split(' ')
            cur_operands = [int(x.strip()) for x in cur_operands_raw if x != '']
            operands_reversed.append(cur_operands)

    operands = []

    for i in range(len(operands_reversed[0])):
        operands.append([x[i] for x in operands_reversed])

    return operands, operations

def compute_grand_total(operands, operations):
    grand_total = 0

    for i in range(len(operands)):
        if operations[i] == '+':
            grand_total += sum(operands[i])
        elif operations[i] == '*':
            grand_total += math.prod(operands[i])

    return grand_total

operands, operations = get_operands(lines)
grand_total = compute_grand_total(operands, operations)

# print(operands, operations)
print(grand_total)