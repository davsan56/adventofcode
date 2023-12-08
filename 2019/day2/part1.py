with open("input.txt", "r") as f:
    content = list(map(lambda x: int(x), f.readline().split(",")))

def operateTwoValues(x, one, two):
    if x == 1:
        return one + two
    elif x == 2:
        return one * two
    else:
        return None

content[1] = 12
content[2] = 2

for i in range(0, len(content), 4):
    intcode = content[i:i+4]
    if intcode[0] == 99:
        break
    toAppend = operateTwoValues(intcode[0], content[intcode[1]], content[intcode[2]])
    if toAppend == None:
        break
    content[intcode[3]] = toAppend
    
print(content)