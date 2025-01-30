import re

with open('./input.txt') as f:
    lines = f.readlines()

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    
res = 0
full_input = ''.join(lines)
# for line in lines:
splits = full_input.split("do()")
for split in splits:
    print(split)
    try:
        patterns = pattern.findall(split[:split.index("don't()")])
        # print(split[:split.index("don't()")])
    except ValueError:
        # print(split)
        patterns = pattern.findall(split)
    for n1, n2 in patterns:
        res += int(n1) * int(n2)
    
print(res)
