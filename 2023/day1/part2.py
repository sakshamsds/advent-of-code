with open('./input.txt') as f:
    lines = f.readlines()

digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def getDigit(line, start, end, increment):
    for i in range(start, end, increment):
        if '0' <= line[i] <= '9':
            return line[i]
        for k, v in digits.items():
            if i + len(k) <= len(line) and k == line[i:i+len(k)]:
                return v

res = 0
for line in lines:
    start = getDigit(line, 0, len(line), 1)
    end = getDigit(line, len(line) - 1, -1, -1)   
    res += int(start + end)         

print(res)