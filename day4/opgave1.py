def findXMAS(array2D: list[list[chr]], x: int, y: int, dir: str = "", count: int = 0) -> int:
    xmasStr: str = "XMAS"

    if count == len(xmasStr):
        return 1
    
    if not(0 <= y < len(array2D)) or not(0 <= x < len(array2D[y])):
        return 0
    
    if array2D[y][x] == xmasStr[count]:
        match dir:
            case "ul":
                return findXMAS(array2D, x - 1, y - 1, "ul" , count + 1)
            case "u":
                return findXMAS(array2D, x    , y - 1, "u"  , count + 1)
            case "ur":
                return findXMAS(array2D, x + 1, y - 1, "ur" , count + 1)
            case "l":
                return findXMAS(array2D, x - 1, y    , "l"  , count + 1)
            case "r":
                return findXMAS(array2D, x + 1, y    , "r"  , count + 1)
            case "dl":
                return findXMAS(array2D, x - 1, y + 1, "dl" , count + 1)
            case "d":
                return findXMAS(array2D, x    , y + 1, "d"  , count + 1)
            case "dr":
                return findXMAS(array2D, x + 1, y + 1, "dr" , count + 1)
            case "":
                return (
                    findXMAS(array2D, x - 1, y - 1, "ul" , count + 1) +
                    findXMAS(array2D, x    , y - 1, "u"  , count + 1) + 
                    findXMAS(array2D, x + 1, y - 1, "ur" , count + 1) + 
                    findXMAS(array2D, x - 1, y    , "l"  , count + 1) + 
                    findXMAS(array2D, x + 1, y    , "r"  , count + 1) + 
                    findXMAS(array2D, x - 1, y + 1, "dl" , count + 1) + 
                    findXMAS(array2D, x    , y + 1, "d"  , count + 1) + 
                    findXMAS(array2D, x + 1, y + 1, "dr" , count + 1) 
                )
            
    return 0

def countAllXMAS(array2D: list[list[chr]]) -> int:
    total_count = 0
    for y in range(len(array2D)):
        for x in range(len(array2D[y])):
            if array2D[y][x] == 'X':
                total_count += findXMAS(array2D, x, y)
    return total_count

with open("day4/inputdata.txt", "r") as f:
    lines = f.readlines()

lines = map(lambda line: line.replace("\n", ""), lines)

splitlines = [list(line) for line in lines]

result = countAllXMAS(splitlines)
print(f"Total 'xmas' found: {result}")