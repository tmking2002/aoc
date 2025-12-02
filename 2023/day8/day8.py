from math import gcd
import math
from functools import reduce

file = open("day8/input.txt", "r")
lines = file.readlines()

directions = str(lines[0].strip()) * 100000

map = {}

# Part 1

for line in lines[2:]:
    origin = line[0:3]
    destination = line[7:15]

    map[origin] = (destination.split(',')[0], destination.split(',')[1].strip())

location = 'AAA'
iterations = 0

#while location != 'ZZZ':
#    direction = directions[iterations]
#    if direction == 'R':
#        location = map[location][1]
#    else:
#        location = map[location][0]
#    iterations += 1

#print(iterations)

# Part 2

locations = [key for key in map.keys() if key.endswith('A')]
iterations = 0

steps = []

for location in locations:
    while location[2] != 'Z':
        direction = directions[iterations]
        if direction == 'R':
            location = map[location][1]
        else:
            location = map[location][0]
        iterations += 1
    print(location)
    steps.append(iterations)
    iterations = 0

print(reduce(math.lcm, steps))
print(steps)
