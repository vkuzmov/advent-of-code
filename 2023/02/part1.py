input = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]

with open('input.txt') as f:
    input = f.readlines()

limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

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

impossible = []

for game_id in parsed:
    for res in parsed[game_id]:
        red = parsed[game_id][res].get('red')
        if red and red > limits['red']:
            impossible.append(game_id)
            continue

        green = parsed[game_id][res].get('green')
        if green and green > limits['green']:
            impossible.append(game_id)
            continue

        blue = parsed[game_id][res].get('blue')
        if blue and blue > limits['blue']:
            impossible.append(game_id)
            continue

possible = parsed.keys() - impossible
print(f'sum: {sum(possible)}')
