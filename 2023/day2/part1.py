import re

constraintDict = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def getValidGame(game_id, line):
    for amt, color in re.findall(r'(\d+) (\w+)', line):
        if constraintDict[color] < int(amt):
            return 0
    return game_id

def main():
    valid_sum = 0
    with open('./input.txt') as f:
        for line in f:
            game_id = int(re.search(r'\d+', line.split(': ')[0]).group())
            valid_sum += getValidGame(game_id, line)
    print(valid_sum)

if __name__ == '__main__':
    main()