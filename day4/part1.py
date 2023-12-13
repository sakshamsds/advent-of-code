import re

with open('./input.txt') as f:
    lines = f.readlines()
    
points = 0
nums_regex = r'\d+'

for line in lines:
    winning_nums, available_nums = [re.findall(nums_regex, part) for part in line.split(': ')[1].split(' | ')]
    matches = len(set(winning_nums) & set(available_nums))
    if matches:
        points += 2 ** (matches - 1) 
    # print(matches)

print(points)   