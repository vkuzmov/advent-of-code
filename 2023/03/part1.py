import re
import sys

# Test mode
try:
    test_mode = (sys.argv[1] == 'test')
except IndexError:
    test_mode = False

def read_numbers(row):
    nums = []
    reading = False
    buffer = ''
    start_idx = 0

    for idx, c in enumerate(row):
        if not is_digit(c) and buffer and reading:
            nums.append({
                'num': int(buffer),
                'start': start_idx,
                'end': idx-1
            })
            buffer = ''
            start_idx = 0
            reading = False
            continue

        if is_digit(c):
            if not reading:
                reading = True
                start_idx = idx
            buffer += c

    if buffer:
        nums.append({
            'num': int(buffer),
            'start': start_idx,
            'end': idx-1
        })

    return nums

def build_matrix(input):
    matrix = []

    for line in input:
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def is_digit(char):
    return re.match(r'\d', char)

def is_symbol(char):
    # symbols = ['*', '@', '+', '$', '#', '&', '%', '/', '=', '-']
    # try:
    #     symbols.index(char)
    #     return True
    # except:
    #     return False

    return not re.match(r'\d|\.', char)

def intersect(x, nums_collection):
    inter_nums = []
    for _, numbers in nums_collection.items():
        print(f'numbers: {numbers}')
        for number in numbers:
            # start number is close to the symbol
            if number['start'] >= x-1 and number['start'] <= x+1:
                inter_nums.append(number['num'])
                continue

            # start number is away from the symbol, but number passes close to the symbol
            if number['start'] < x-1 and (number['start'] + len(str(number['num']))-1) >= x-1:
                inter_nums.append(number['num'])
                continue

            # # end number is close to the symbol
            # if number['end'] >= x-1 and number['end'] <= x+1:
            #     inter_nums.append(number['num'])
            #     continue

    return inter_nums

def main():
    input = read_input()
    # print(input)

    matrix = build_matrix(input)
    # print(matrix)

    part_numbers = []

    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if not is_symbol(char):
                continue

            print(f'({y}, {x}): {char}')
            nums = {}

            if y > 0:
                prev_nums = read_numbers(matrix[y-1])
                if prev_nums:
                    nums[y-1] = prev_nums

            curr_nums = read_numbers(matrix[y])
            if curr_nums:
                nums[y] = curr_nums

            if y+1 < len(matrix):
                next_nums = read_numbers(matrix[y+1])
                if next_nums:
                    nums[y+1] = next_nums

            # print(nums)
            inter = intersect(x, nums)
            print(inter)
            print('-----------------------------------')
            part_numbers.extend(inter)

    print(part_numbers)
    print(f'the answer is: {sum(part_numbers)}')

def read_input():
    input = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..',
    ]
    if test_mode:
        return input

    with open('input.txt') as f:
        input = [line.rstrip() for line in f]

    return input

if __name__ == "__main__":
    main()


#     0 1 2 3 4 5 6 7 8 9
# -----------------------
# 0 | 4 6 7 . . 1 1 4 . .
# 1 | . . . * . . . . . .
# 2 | . . 3 5 . . 6 3 3 .
# 3 | . . . . . . # . . .
# 4 | 6 1 7 * . . . . . .
# 5 | . . . . . + . 5 8 .
# 6 | . . 5 9 2 . . . . .
# 7 | . . . . . . 7 5 5 .
# 8 | . . . $ . * . . . .
# 9 | . 6 6 4 . 5 9 8 . .
# -----------------------
#     0 1 2 3 4 5 6 7 8 9

# 536993
# 586462
# 539590
