import re
import sys

input = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

with open('input.txt') as f:
    input = f.readlines()

output = []

mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def replacer(line):
    if len(line) == 0:
        return ''

    word = ''
    for index in range(len(line)):
        c = line[index]
        word += c
        if mapping.get(word):
            return mapping.get(word) + replacer(line[len(word):])

    return word[0] + replacer(word[1:])

for line in input:
    print(line.strip("\n"))
    s = replacer(line)
    print(s.strip("\n"))
    a = re.findall(r'\d', s)
    print(a)
    num = int(a[0]+a[-1])
    print(num)
    output.append(num)
    print('----------')

print(output)
sum = sum(output)
print(f"sum: {sum}")
