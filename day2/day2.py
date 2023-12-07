import time
import re
# red, green or blue cube
# each line has a random number of each colored cube
# which game would be possible if it only had a max of 12 red, 13 green and 14 blue
# Get all the id's of which it's possible to play the game 

# timer for functions
def timer(func):
    n = 10000
    t0 = time.time()
    for n in range(n): func
    t1 = time.time()
    return t1-t0

def part1():
    arr = []
    allNumbers = []

    colors = ["red", "green", "blue"]
    startOfGame = ":"
    newSet = ","
    endOfGame = ";"
    with open('./input.txt') as file:
        while line := file.readline():
            line.rstrip()
            allNumbers.append(re.findall(r'[\d]+', line))
            arr.append(''.join(' '+x if 'A' <= 'Z' else x for x in line.replace(u'\xa0', '')).rstrip())
            # arr.append(line)
    file.close()

    # for number in allNumbers:
    #     print("id", number[0])
    print(arr)
part1()