import pandas as pd
import itertools
import time

file = open("day7/input.txt", "r")
lines = file.readlines()

cards = [line[0:5] for line in lines]
bets = [int(line[6:].replace('\n', '')) for line in lines]

# Part 1

part1_start = time.time()

score_map = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}

def find_hand(og_cards):
    cards = og_cards.split()
    cards = [card[0] for card in og_cards]
    
    card_values = [score_map[card] for card in cards]

    hand_counts = [cards.count(card) for card in cards]
    hand_counts.sort(reverse=True)

    if 5 in hand_counts:
        hand = 6
    elif 4 in hand_counts:
        hand = 5
    elif 3 in hand_counts and 2 in hand_counts:
        hand = 4
    elif 3 in hand_counts:
        hand = 3
    elif hand_counts[2] == 2:
        hand = 2
    elif 2 in hand_counts:
        hand = 1
    else:
        hand = 0

    hand_value = str(hand) + (chr(ord('@')+card_values[0])) + (chr(ord('@')+card_values[1])) + (chr(ord('@')+card_values[2])) + (chr(ord('@')+card_values[3])) + (chr(ord('@')+card_values[4]))
    return hand_value
        
    
hand_values = [find_hand(cards) for cards in cards]

hands_df = pd.DataFrame({"bet": bets, "hand_values": hand_values})
hands_df = hands_df.sort_values(by=['hand_values', 'bet'], ascending=True).reset_index(drop=True)

hands_df['winnings'] = (hands_df.index + 1) * hands_df['bet']

print(sum(hands_df['winnings']))
print("Part 1 time: ", time.time() - part1_start)

# Part 2

part2_start = time.time()

score_map = {"A": 13, "K": 12, "Q": 11, "J": 0, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}

def find_hand(og_cards):

    cards = og_cards.split()
    cards = [card[0] for card in og_cards]

    card_values = [score_map[card] for card in cards]

    hand_counts = [cards.count(card) for card in cards]
    
    hand_counts.sort(reverse=True)

    if cards.count('J') == 0:
        if 5 in hand_counts:
            hand = 6
        elif 4 in hand_counts:
            hand = 5
        elif 3 in hand_counts and 2 in hand_counts:
            hand = 4
        elif 3 in hand_counts:
            hand = 3
        elif hand_counts[2] == 2:
            hand = 2
        elif 2 in hand_counts:
            hand = 1
        else:
            hand = 0

        hand_value = str(hand) + (chr(ord('@')+card_values[0])) + (chr(ord('@')+card_values[1])) + (chr(ord('@')+card_values[2])) + (chr(ord('@')+card_values[3])) + (chr(ord('@')+card_values[4]))
        return hand_value

    joker_locs = [i for i, card in enumerate(cards) if card == 'J']
    
    hand_values = []

    for _ in range(len(joker_locs)):
        combos = itertools.product(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'], repeat=len(joker_locs))
        
        for combo in combos:
            temp_cards = cards.copy()
            
            for replacement, joker_loc in zip(combo, joker_locs):
                temp_cards[joker_loc] = replacement

            hand_counts = [temp_cards.count(card) for card in temp_cards]
            hand_counts.sort(reverse=True)

            if 5 in hand_counts:
                hand = 6
            elif 4 in hand_counts:
                hand = 5
            elif 3 in hand_counts and 2 in hand_counts:
                hand = 4
            elif 3 in hand_counts:
                hand = 3
            elif hand_counts[2] == 2:
                hand = 2
            elif 2 in hand_counts:
                hand = 1
            else:
                hand = 0

            hand_value = str(hand) + (chr(ord('@')+card_values[0])) + (chr(ord('@')+card_values[1])) + (chr(ord('@')+card_values[2])) + (chr(ord('@')+card_values[3])) + (chr(ord('@')+card_values[4]))

            hand_values.append(hand_value)

    hand_value = max(hand_values)

    return hand_value
        

hand_values = [find_hand(cards) for cards in cards]

hands_df = pd.DataFrame({"bet": bets, "hand_values": hand_values})
hands_df = hands_df.sort_values(by=['hand_values', 'bet'], ascending=True).reset_index(drop=True)

hands_df['winnings'] = (hands_df.index + 1) * hands_df['bet']

print(sum(hands_df['winnings']))

print("Part 2 time: ", time.time() - part2_start)