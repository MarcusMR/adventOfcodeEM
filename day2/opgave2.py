def is_safe(levels):
    if len(levels) < 2:  # Not enough data to determine safety
        return False

    increasing = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        if increasing:
            if not (levels[i] < levels[i + 1] and 1 <= abs(levels[i] - levels[i + 1]) <= 3):
                return False
        else:
            if not (levels[i] > levels[i + 1] and 1 <= abs(levels[i] - levels[i + 1]) <= 3):
                return False
    return True

with open("day2/inputdata.txt", "r") as f:
    data = f.readlines()

safeCount = 0

for line in data:
    levels = list(map(int, line.split()))

    if is_safe(levels):
        safeCount += 1
    else:
        for i in range(len(levels)):
            tmp = levels[:i] + levels[i + 1:]
            if is_safe(tmp):
                safeCount += 1
                break

print(safeCount)
