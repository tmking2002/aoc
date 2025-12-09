import numpy as np

test = False

if test == True:
    input_path = 'day8/sample.txt'
else:
    input_path = 'day8/input.txt'

with open(input_path) as f:
    data = f.read()
    coordinates = data.split('\n')

coordinates = [
    (int(coord.split(',')[0]), 
     int(coord.split(',')[1]), 
     int(coord.split(',')[2])) for coord in coordinates]

def euclidean(x1, y1, z1, x2, y2, z2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def calculate_distances(coordinates):
    distances = {}
    for i, x in enumerate(coordinates):
        for j, y in enumerate(coordinates):
            if i >= j:
                continue
            distances[(i, j)] = euclidean(x[0], x[1], x[2], y[0], y[1], y[2])
    return distances

def calculate_circuits(prev_circuits, new_pair):
    circ_1 = circ_2 = None

    for idx, circuit in enumerate(prev_circuits):
        if circ_1 is None and new_pair[0] in circuit:
            circ_1 = idx
        if circ_2 is None and new_pair[1] in circuit:
            circ_2 = idx
        if circ_1 is not None and circ_2 is not None:
            break

    if circ_1 == circ_2:
        return prev_circuits
    else:
        new_circuits = prev_circuits
        new_circuits[circ_1].extend(new_circuits[circ_2])
        del new_circuits[circ_2]

        return new_circuits

def calculate_answer(final_pair):
    coord1 = coordinates[final_pair[0]]
    coord2 = coordinates[final_pair[1]]

    return coord1[0] * coord2[0]

circuits = [[i] for i, coord in enumerate(coordinates)]

distances = calculate_distances(coordinates)
sorted_distances = sorted(distances.items(), key=lambda item: item[1])

distances_dict = dict(sorted_distances)

for pair, _ in distances_dict.items():
    circuits = calculate_circuits(circuits, pair)
    if len(circuits) == 1:
        break

answer = calculate_answer(pair)
print(answer)