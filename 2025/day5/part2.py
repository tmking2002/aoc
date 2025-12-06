test = False

if test == True:
    input_path = 'day5/sample.txt'
else:
    input_path = 'day5/input.txt'

with open(input_path) as f:
    data = f.read()
    id_ranges, available_ids = data.split('\n\n')
    ranges = id_ranges.split('\n')
    ids = available_ids.split('\n')

def adjust_ranges(ranges):
    range_list = []
    for range in ranges:
        range_list.append((int(range.split('-')[0]), int(range.split('-')[1])))
    return sorted(range_list)

def simplify_ranges(range_list):
    
    iter = 0
    while True:
        to_remove = set()
        to_add = set()
        removals_iter = False
        for i, cur_tuple in enumerate(range_list):

            if i == (len(range_list) - 1):
                break

            next_tuple = range_list[i+1]

            if (next_tuple[0] <= cur_tuple[1]) & (next_tuple[1] <= cur_tuple[1]):
                to_remove.add(next_tuple)
                removals_iter = True

            elif (next_tuple[0] <= cur_tuple[1]):
                to_remove.add(cur_tuple)
                to_remove.add(next_tuple)

                to_add.add((cur_tuple[0], next_tuple[1]))

                removals_iter = True

        # print(to_remove, to_add)
        # print(range_list)
        # print()

        for remove in to_remove:
            range_list.remove(remove)

        for add in to_add:
            range_list.append(add)

        range_list = sorted(range_list)
        iter += 1

        if removals_iter == False:
            break

    return sorted(range_list)


range_list = adjust_ranges(ranges)    
simplified_range_list = simplify_ranges(range_list)

# print(simplified_range_list)

sum = 0

for range in simplified_range_list:
    sum += (range[1] - range[0] + 1)

print(sum)