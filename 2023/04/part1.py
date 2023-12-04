import re
import sys

# Test mode
try:
    test_mode = (sys.argv[1] == 'test')
except IndexError:
    test_mode = False

def read_cards(input):
    cards = {}
    for line in input:
        card = {}
        card = line.split(': ')
        card_id = int(card[0].replace('Card ', ''))
        numbers = card[1].split(' | ')
        cards[card_id] = {
            'winning': set(map(lambda x: int(x), re.findall(r'\d+', numbers[0]))),
            'numbers': set(map(lambda x: int(x), re.findall(r'\d+', numbers[1]))),
        }

    return cards

def main():
    input = read_input()
    # print(input)

    cards = read_cards(input)
    print('-------------------------------')

    total_points = 0
    for card_id, card in cards.items():
        # print(card_id, card)
        winners = card['winning'].intersection(card['numbers'])

        points = 0
        if len(winners):
            points = pow(2, len(winners)-1)
        card['points'] = points
        total_points += points

    print(f'the answer is: {total_points}')

def read_input():
    input = [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
    ]
    if test_mode:
        return input

    with open('input.txt') as f:
        input = [line.rstrip() for line in f]

    return input

if __name__ == "__main__":
    main()
