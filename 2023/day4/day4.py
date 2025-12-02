import re
import pandas as pd

file = open("day4/input.txt", "r")
lines = file.readlines()

# Part 1

points = 0

for line in lines:

    split_line = re.split(r'\||:', line)
    winning_numbers = pd.to_numeric(re.findall(r'\d+', split_line[1]))
    my_numbers = pd.to_numeric(re.findall(r'\d+', split_line[2]))
    
    num_wins = 0

    for i in winning_numbers:
        if i in my_numbers and num_wins == 0:
            num_wins += 1
        elif i in my_numbers and num_wins != 0:
            num_wins *= 2
    
    points += num_wins

print(points)

# Part 2

num_cards = {}
num_cards[1] = 1

for line in lines:

    split_line = re.split(r'\||:', line)
    card_number = pd.to_numeric(re.findall(r'\d+', split_line[0]))[0]
    winning_numbers = pd.to_numeric(re.findall(r'\d+', split_line[1]))
    my_numbers = pd.to_numeric(re.findall(r'\d+', split_line[2]))

    if (card_number) not in num_cards:
        num_cards[card_number] = 1 

    num_matches = 0

    for i in winning_numbers:
        if i in my_numbers:
            num_matches += 1

    for i in range(1, num_matches + 1):
        if (i + card_number) not in num_cards:
            num_cards[i + card_number] = 1 
        num_cards[i + card_number] += num_cards[card_number]

print(sum(num_cards.values()))
    

