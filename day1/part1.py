# with open('./input.txt') as f:
#     lines = f.readlines()

# # print(len(lines))       # 1000

# def getDigit(line):
#     for char in line:
#         if '0' <= char <= '9':
#             return char
#     return '-1'

# res = 0
# for line in lines:
#     start = getDigit(line)
#     end = getDigit(line[::-1])   
#     res += int(start + end)         

# print(res)

# optimized
import re

with open('./input.txt') as f:
    lines = f.readlines()

digit_pattern = re.compile(r'\d')

res = 0
for line in lines:
    digits = digit_pattern.findall(line)
    print(digits)
    if digits:
        res += int(digits[0] + digits[-1])

print(res)
