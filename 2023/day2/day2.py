import re
import pandas as pd

file = open("day2/input.txt", "r")
lines = file.readlines()

impossible_games = []
last_game_id = 0
sum_power = 0

for line in lines:
    game_id = pd.to_numeric(re.findall(r'Game (\d+)', line))[0]
    last_game_id = game_id

    min_green = 0
    min_red = 0
    min_blue = 0

    subgames = line.split(";")
    for subgame in subgames:
        green = pd.to_numeric(re.findall(r'(\d+) green', subgame))
        red = pd.to_numeric(re.findall(r'(\d+) red', subgame))
        blue = pd.to_numeric(re.findall(r'(\d+) blue', subgame))

        if green.size == 0:
            green = 0
        if red.size == 0:
            red = 0
        if blue.size == 0:
            blue = 0

        if green > 13 or red > 12 or blue > 14:
            impossible_games.append(game_id)

        if green > min_green:
            min_green = green
        if red > min_red:
            min_red = red
        if blue > min_blue:
            min_blue = blue

    power = min_green * min_red * min_blue
    sum_power += power

    min_green = 0
    min_red = 0
    min_blue = 0


possible_games = [game_id for game_id in range(1, last_game_id + 1) if game_id not in impossible_games]
print(sum(possible_games))
print(sum_power)