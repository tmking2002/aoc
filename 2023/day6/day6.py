import numpy as np
import re
import math

file = open("day6/input.txt", "r")
lines = file.readlines()

# Part 1

times = re.findall(r'\d+', lines[0])
times = [int(num) for num in times]

distances = re.findall(r'\d+', lines[1])
distances = [int(num) for num in distances]

records = zip(times, distances)

total_ways = []

for time, distance in records:
    dist_covered = [0, time - 1]
    for i in range(2, time + 1):
        dist_covered.append(dist_covered[i-1] + dist_covered[1] - (2 * (i - 1)))

    win = [int(val > distance) for val in dist_covered]
    
    total_ways.append(sum(win))

print(np.prod(total_ways))

# Part 2

time = int(re.findall(r'\d+', lines[0].replace(' ', ''))[0])

distance = int(re.findall(r'\d+', lines[1].replace(' ', ''))[0])

a = -1
b = time + 2
c = -1 * (time + distance + 1)

sol1 = math.ceil((-b + math.sqrt(b**2 - 4*a*c)) / (2 * a))
sol2 = math.ceil((-b - math.sqrt(b**2 - 4*a*c)) / (2 * a))

print(sol2 - sol1)

