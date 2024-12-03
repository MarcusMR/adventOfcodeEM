import re

def mul(a, b):
    return a * b

with open("day3/inputdata.txt", "r") as f:
    data = f.read()
    
mult: list = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)

mult2 = sum(map(eval, mult))

print(mult2)


