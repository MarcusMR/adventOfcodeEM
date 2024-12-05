with open("day5/inputdata.txt", "r") as f:
    input_rules = f.readlines()
with open("day5/inputdata2.txt", "r") as f:
    updates = f.readlines()

# Parsing
ordering = [line.strip().split("|") for line in input_rules]
orderDict = {}
for rule in ordering:
    if rule[0] not in orderDict:
        orderDict[rule[0]] = []
    orderDict[rule[0]].append(rule[1])

updates = [line.strip().split(",") for line in updates]

# Validate updates
def is_valid_update(update, orderDict):
    for i, num in enumerate(update):
        if num in orderDict:
            for dependent in orderDict[num]:
                if dependent in update and update.index(dependent) < i:
                    return False
    return True

# Process updates
valid_updates = [update for update in updates if is_valid_update(update, orderDict)]
middle_values = [int(update[len(update) // 2]) for update in valid_updates]

# Result
print(sum(middle_values))
