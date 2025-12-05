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

def check_fresh(id, range_list):
    
    for range in range_list:
        if (id >= range[0]) & (id <= range[1]):
            return True
        
    return False

range_list = adjust_ranges(ranges)    
fresh_count = sum([check_fresh(int(id), range_list) for id in ids])

print(fresh_count)