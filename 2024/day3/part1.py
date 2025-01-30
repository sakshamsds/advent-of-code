import re

with open('./input.txt') as f:
    lines = f.readlines()

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    
res = 0
for line in lines:
    patterns = pattern.findall(line)
    for n1, n2 in patterns:
        res += int(n1) * int(n2)
    
print(res)
