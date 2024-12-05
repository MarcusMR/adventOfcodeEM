with open("day5/inputdata.txt", "r") as f:
    input_rules = f.readlines()
with open("day5/inputdata2.txt", "r") as f:
    updates = f.readlines()

ordering = [line.strip().split("|") for line in input_rules]
orderDict = {}
for rule in ordering:
    if rule[0] not in orderDict:
        orderDict[rule[0]] = []
    orderDict[rule[0]].append(rule[1])

updates = [line.strip().split(",") for line in updates]

notValid = []

def is_valid_update(update, orderDict):
    for i, num in enumerate(update):
        if num in orderDict:
            for dependent in orderDict[num]:
                if dependent in update and update.index(dependent) < i:
                    return False
    return True

def fixNotValidUpdate(update, orderDict):
    print("before", update)
    while not is_valid_update(update, orderDict):
        for i, num in enumerate(update):
            if num in orderDict:
                for dependent in orderDict[num]:
                    if dependent in update:
                        dep_index = update.index(dependent)
                        if dep_index < i:
                            update[i], update[dep_index] = update[dep_index], update[i]
                            print("inbeween", update)

    print("after", update)
    return update

notvalid_updates = [update for update in updates if not is_valid_update(update, orderDict)]

corrected_updates = [fixNotValidUpdate(update, orderDict) for update in notvalid_updates]

middle_not_values = [int(update[len(update) // 2]) for update in corrected_updates]

print("Sum of middle values for corrected updates:", sum(middle_not_values))

print(sum(middle_not_values))