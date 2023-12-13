
uniques = set()

with open('./input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        for char in line:
            if not char.isdigit() and char not in uniques:
                uniques.add(char)

    print(uniques)