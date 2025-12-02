import re
import pandas as pd

file = open("day5/input.txt", "r")
lines = file.readlines()

seeds_p1 = pd.to_numeric(lines[0].replace('seeds: ', '').split(' '))

maps = {}
nums = []

for line in lines[2:]:
    if re.findall(r'[a-z]', line):
        if len(nums) > 0:
            maps[map_label] = nums
        map_label = ''.join(x for x in line if x.isalpha() or x.isspace() or x == '-').strip()
        nums = []
    elif re.findall(r'[0-9]', line):
        dest_start = pd.to_numeric(line.split(' ')[0])
        source_start = pd.to_numeric(line.split(' ')[1])
        range_len = pd.to_numeric(line.split(' ')[2])
        
        nums.append((dest_start, source_start, range_len))

maps[map_label] = nums

def map_value(initial, map):
    for map_tuple in map:
        destination_start, source_start, range_len = map_tuple

        if initial >= source_start and initial <= source_start + range_len - 1:
            new = initial + (destination_start - source_start)
            break
        else:
            new = initial

    return new

def map_range(initial_start, initial_end, map):
    possible_ranges = []

    for map_tuple in map:
        destination_start, source_start, range_len = map_tuple
        source_end = destination_start + range_len - 1

        if (initial_start >= source_end) or (initial_end <= source_start):
            new_start = initial_start
            new_end = initial_end
        if initial_start < source_end:
            new_start = initial_start
            new_end = min(initial_end, source_start)
        if initial_end > source_start:
            new_start = max(initial_start, source_end)
            new_end = initial_end
    
    possible_ranges += [(new_start, new_end)]

    return list(set(possible_ranges))

min_location_p1 = float('inf')
min_location_p2 = float('inf')

for seed in seeds_p1:
    step = seed
    for map_label, map_values in maps.items():
        step = map_value(step, map_values)
    location = step
    if location < min_location_p1:
        min_location_p1 = location

for index, seed in enumerate(seeds_p1):
    if index % 2 == 0:
        continue

    ranges = [(seeds_p1[index - 1], seeds_p1[index - 1] + seed - 1)]

    for map_label, map_values in maps.items():
        new_ranges = []
        for range in ranges:
            new_ranges += map_range(range[0], range[1], map_values)
        #print(map_label, new_ranges)
        ranges = new_ranges

    location = min(tuple_[0] for tuple_ in new_ranges)
    if location < min_location_p2:
        min_location_p2 = location


print(min_location_p1)
print(min_location_p2)