with open("day4/inputdata.txt", "r") as f:
    lines = f.readlines()

lines = map(lambda line: line.replace("\n", ""), lines)

splitlines = [list(line) for line in lines]

count = 0

for y, line in enumerate(splitlines):
    for x, char in enumerate(line):
        if char == "A":
            if (
                x + 1 < len(line) and x - 1 >= 0 and
                y + 1 < len(splitlines) and y - 1 >= 0
            ):
                hoejreUp = splitlines[y+1][x+1]
                hoejreDown = splitlines[y-1][x+1]
                venstreUp = splitlines[y+1][x-1]
                venstreDown = splitlines[y-1][x-1]

                if hoejreUp == "M" and venstreDown == "S" and hoejreDown == "M" and venstreUp == "S":
                    count += 1
                if hoejreUp == "S" and venstreDown == "M" and hoejreDown == "M" and venstreUp == "S":
                    count += 1
                if hoejreUp == "S" and venstreDown == "M" and hoejreDown == "S" and venstreUp == "M":
                    count += 1
                if hoejreUp == "M" and venstreDown == "S" and hoejreDown == "S" and venstreUp == "M":
                    count += 1
print(count)