import re

def mul(a, b):
    return a * b

with open("day3/inputdata.txt", "r") as f:
    data = f.read()
    
mult: list = re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", data)

print(mult)

marcus: bool = True
marcuslist = []

for x in mult:
    if x == "do()":
        marcus = True
        continue
    elif x == "don't()":
        marcus = False

    if marcus == True:
        marcuslist.append(eval(x))



print(sum(marcuslist))


