with open("/home/marcus/advent/day1/inputdata.txt", "r") as f:
    data = f.readlines()

linelist: list = []
linelist2: list = []

for line in data:
    text = line.replace("\n", "").split("  ")
    linelist.append(int(text[0]))
    linelist2.append(int(text[1]))

linelist.sort()
linelist2.sort()

resNum = 0

for l, l2 in zip(linelist, linelist2):
    
    resNum += abs(l2 - l) 

print(resNum)

numdict = {}
numdict2 = {}

for l, l2 in zip(linelist, linelist2):
    
    if l in numdict.keys():
        numdict[l] += 1
    else:
        numdict[l] = 1

    if l2 in numdict2.keys():
        numdict2[l2] += 1
    else:
        numdict2[l2] = 1 

sum = 0

for x in numdict.keys():
    if x in numdict2:
        sum += numdict2[x] * x

print(sum)