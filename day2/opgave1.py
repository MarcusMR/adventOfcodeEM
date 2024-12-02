with open("day2/inputdata.txt", "r") as f:
    data = f.readlines()

safeCount = 0

for line in data:
    splitLine = []
    lineData = line.split(" ")
    for number in lineData:
        splitLine.append(int(number))

    passport = True
    if splitLine[0] > splitLine[1]:
        for i in range(len(splitLine)-1):
            if not (splitLine[i] > splitLine[i+1] and abs(splitLine[i] - splitLine[i+1]) <= 3 and abs(splitLine[i] - splitLine[i+1]) >= 1):
                passport = False
    elif splitLine[0] < splitLine[1]:
        for i in range(len(splitLine)-1):
            if not (splitLine[i] < splitLine[i+1] and abs(splitLine[i] - splitLine[i+1]) <= 3 and abs(splitLine[i] - splitLine[i+1]) >= 1):
                passport = False
    else:
        passport = False
    if passport:
        safeCount += 1 

print(safeCount)
