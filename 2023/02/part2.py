input = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]

with open('input.txt') as f:
    input = [line.rstrip() for line in f]

parsed = {}

for line in input:
    game = line.split(': ')
    game_id = int(game[0].replace('Game ', ''))
    outcomes = game[1].split('; ')

    parsed[game_id] = {}
    outcome_cnt = 0

    for outcome in outcomes:
        cubes = outcome.split(', ')
        parsed[game_id][outcome_cnt] = {}
        for cube in cubes:
            (cnt, color) = cube.split(' ')
            parsed[game_id][outcome_cnt][color] = int(cnt)
        outcome_cnt += 1

min_possible = {}

for game_id in parsed:
    min_possible[game_id] = {'red': 1, 'green': 1, 'blue': 1}

    for res in parsed[game_id]:
        red = parsed[game_id][res].get('red')
        if red and red > min_possible[game_id]['red']:
            min_possible[game_id]['red'] = red

        green = parsed[game_id][res].get('green')
        if green and green > min_possible[game_id]['green']:
            min_possible[game_id]['green'] = green

        blue = parsed[game_id][res].get('blue')
        if blue and blue > min_possible[game_id]['blue']:
            min_possible[game_id]['blue'] = blue

min_possible_flat = []

for (key,value) in min_possible.items():
    min_possible_flat.append(value['red'] * value['green'] * value['blue'])

print(min_possible_flat)
print(f'sum: {sum(min_possible_flat)}')
