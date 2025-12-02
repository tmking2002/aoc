file = open("day1/input.txt", "r")
lines = file.readlines()

part1 = 0
part2 = 0

for line in lines:
    part1_digits = []
    part2_digits = []

    for i, char in enumerate(line):
        if(char.isdigit()):
            part1_digits.append(char)
            part2_digits.append(char)
        
        for digit, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if(line[i:].startswith(value)):
                part2_digits.append(str(digit + 1))
                break

    part1_digits = part1_digits[0] + part1_digits[-1]
    part2_digits = part2_digits[0] + part2_digits[-1]

    part1 += int(part1_digits)
    part2 += int(part2_digits)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))