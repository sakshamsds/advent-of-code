'''
1   =1
2   +1  =2
3   +1  +2  =4
4   +1  +2  +4  =8
5   +1  +4  +8  =14
6   
'''

import re

with open('./input.txt') as f:
    lines = f.readlines()
    
points = 0
nums_regex = r'\d+'
copies = [1] * len(lines)

for i, line in enumerate(lines):
    winning_nums, available_nums = [set(re.findall(nums_regex, part)) for part in line.split(': ')[1].split(' | ')]
    num_matches = len(winning_nums & available_nums)
    
    for j in range(i + 1, i + 1 + num_matches):
        copies[j] += copies[i] 

print(sum(copies))   