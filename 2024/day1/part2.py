import re
import collections

with open('./input.txt') as f:
    lines = f.readlines()

number_pattern = re.compile(r'\d+')

l1, l2_freqs = [], collections.defaultdict(int)
for line in lines:
    nums = number_pattern.findall(line)
    l1.append(int(nums[0]))
    l2_freqs[int(nums[1])] += 1

similarity_score = 0
for num in l1:
    similarity_score += num * l2_freqs[num]

print(similarity_score)