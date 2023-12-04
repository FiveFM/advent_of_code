import re
import time

# timer for functions
def timer(func):
    n = 10000
    t0 = time.time()
    for i in range(n): func
    t1 = time.time()
    return t1-t0

def part1():
    numbers = []
    sum = 0
    with open('./input.txt') as file:
        while line := file.readline():           
            numbers.append(re.findall(r'[\d]+', line))
    file.close()

    for number in numbers:
            a = number[0][0] + number[-1][-1]
            sum += int(a)

    return sum

def part2():
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    sum = 0

    with open('./input.txt') as file:
        while line := file.readline():
            line.rstrip()
            indexes = []
            for digit in digits:
                numWords = re.finditer(digit, line)
                indexes.extend([{'value': digit, 'index': numWord.start()} for numWord in numWords])
            
            for index, char in enumerate(line):
                 if char.isdigit():
                      indexes.append({'value': char, 'index': index})            
            
            if indexes:
                first = min(indexes, key=lambda x: x['index'])['value']
                last = max(indexes, key=lambda x: x['index'])['value']

                if first.isdigit() and last.isdigit():
                    fullNumber = first + last
                elif not first.isdigit() and last.isdigit():
                    fullNumber = str(digits.index(first) + 1) + last
                elif first.isdigit() and not last.isdigit():
                    fullNumber = first + str(digits.index(last) + 1)
                else:
                    fullNumber = str(digits.index(first) + 1) + str(digits.index(last) + 1)   
    
                sum += int(fullNumber)
    file.close()

    return sum

print("solution part 1: ", part1(), " time: ", timer(part1()))
print("solution part 2: ", part2(), " time: ", timer(part2()))