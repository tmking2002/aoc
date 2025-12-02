file = open('day9/input.txt', 'r')
lines = file.readlines()

# Part 1

def extrapolate(line):
    history = []
    numbers = [int(number) for number in line.split(' ')]
    new_numbers = []

    history = [numbers]
    
    while not all(value == 0 for value in history[-1]):

        for i in range(0, len(numbers) - 1):
            new_numbers.append(numbers[i + 1] - numbers[i])
        
        history.append(new_numbers)
        numbers = new_numbers.copy()
        new_numbers = []

    row = len(history) - 2

    while row >= 0:
        history[row].append(history[row + 1][-1] + history[row][-1])
        row -= 1

    return history[0][-1]

extrapolations = []

for line in lines:
    extrapolations.append(extrapolate(line.strip()))

print(sum(extrapolations))

# Part 2

def extrapolate_backwards(line):
    history = []
    numbers = [int(number) for number in line.split(' ')]
    new_numbers = []

    history = [numbers]
    
    while not all(value == 0 for value in history[-1]):

        for i in range(0, len(numbers) - 1):
            new_numbers.append(numbers[i + 1] - numbers[i])
        
        history.append(new_numbers)
        numbers = new_numbers.copy()
        new_numbers = []
    
    row = len(history) - 2

    history[-1].insert(0, 0)

    while row >= 0:
        history[row].insert(0, history[row][0] - history[row + 1][0])
        row -= 1

    return history[0][0]

extrapolations = []

for line in lines:
    extrapolations.append(extrapolate_backwards(line.strip()))

print(sum(extrapolations))