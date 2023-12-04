
# for every line, get start and end
# check if symbol is found in nbrs
# add to res

symbols = {'/', '%', '+', '-', '$', '&', '#', '@', '=', '*'}

def is_valid_position(r, c):
    return 0 <= r < rows and 0 <= c < cols and lines[r][c] in symbols

def is_valid(s, e, r):
    if is_valid_position(r, s - 1):     # check left nbr
        return True
    if is_valid_position(r, e + 1):     # check right nbr
        return True
    for i in range(s - 1, e + 2):       # check nbrs above and below
        if is_valid_position(r - 1, i) or is_valid_position(r + 1, i):
            return True
    return False

with open('input.txt') as f:
# with open('test_input.txt') as f:
    lines = f.readlines()
    rows, cols = len(lines), len(lines[0]) - 1
    res = 0

for r, line in enumerate(lines):
    line = line.strip()
    c = 0
    while c < cols:
        # print(line, '\t', c)
        if line[c].isdigit():
            num = ''
            s = c
            while c < cols and line[c].isdigit():
                num += line[c]
                c += 1
            if is_valid(s, c - 1, r):
                # print(num)
                res += int(num)
        c += 1
print(res)