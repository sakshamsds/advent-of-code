import re

with open('./input.txt') as f:
    lines = f.readlines()

number_pattern = re.compile(r'\d+')

l1, l2 = [], []
for line in lines:
    nums = number_pattern.findall(line)
    l1.append(int(nums[0]))
    l2.append(int(nums[1]))

l1.sort()
l2.sort()

total_distance = 0
for n1, n2 in zip(l1, l2):
    total_distance += abs(n2 - n1)

print(total_distance)
