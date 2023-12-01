import re

input = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
    'eight412372srvbfive',
]

with open('input.txt') as f:
    input = f.readlines()

output = []

for line in input:
    a = re.findall(r'\d', line)
    num = int(a[0]+a[-1])
    output.append(int(num))

print(output)
sum = sum(output)
print(f"sum: {sum}")
