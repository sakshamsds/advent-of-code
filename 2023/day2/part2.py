import math
import re
import collections

def getPower(line):
    game = collections.defaultdict(int)
    for amt, color in re.findall(r'(\d+) (\w+)', line):
        game[color] = max(game[color], int(amt))
    return math.prod(game.values())

def main():
    total_power = 0
    with open('./input.txt') as f:
        for line in f:
            total_power += getPower(line)
    print(total_power)

if __name__ == '__main__':
    main()