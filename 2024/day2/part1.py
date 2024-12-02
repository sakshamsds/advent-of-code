
with open('./input.txt') as f:
    lines = f.readlines()
    
def isSafe(arr):
    pos, neg = 0, 0
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if abs(diff) > 3 or diff == 0:
            return 0
        if diff < 0:
            neg += 1
        else:
            pos += 1
    # print(arr, pos, neg)
    if pos == len(arr) - 1 or neg >= len(arr) - 1:
        return 1
    return 0
    
num_safe = 0
for line in lines:
    nums = list(map(int, line.split()))
    num_safe += isSafe(nums)

print(num_safe)
