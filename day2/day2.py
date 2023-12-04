import time

# timer for functions
def timer(func):
    n = 10000
    t0 = time.time()
    for n in range(n): func
    t1 = time.time()
    return t1-t0

def part1():
    with open('./input.txt') as file:
        while line := file.readline():
            line.rstrip()
            print(line)
part1()