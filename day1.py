import re
import time

def part1():
    numbers = []
    sum = 0
    with open('./input_day1.txt') as file:
        while line := file.readline():
            numbers.append(re.findall(r'[\d]+', line))
    file.close()

    for number in numbers:
            a = number[0][0] + number[-1][-1]
            sum += int(a)

    return sum

def part2():
    print("do something")

n = 10000
t0 = time.time()
for i in range(n): part1
t1 = time.time()

print(t1-t0)
print(part1())