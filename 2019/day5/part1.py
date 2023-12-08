from enum import Enum

with open("input.txt", "r") as f:
    content = list(map(lambda x: int(x), f.readline().split(",")))

class Op(Enum):
    ADD=1
    MULTIPLY=2
    POSITION=3
    VALUE=4
    STOP=9

def getInstruction(x):
    string = str(x)
    fivestring = string.zfill(5)
    return Op(int(fivestring[4]))

def getPositionOrValue(instruction, param, position):
    string = str(instruction)
    fivestring = string.zfill(5)
    posOrVal = fivestring[position]
    if posOrVal == "0":
        return content[param]
    else:
        return param

i = -1
while True:
    i += 1
    instruction = content[i]
    op = getInstruction(content[i])
    if op == Op.ADD:
        print(content[i:i+4])
        i += 1
        param1 = content[i]
        param1 = getPositionOrValue(instruction, param1, 2)
        i += 1
        param2 = content[i]
        param2 = getPositionOrValue(instruction, param2, 1)
        i += 1
        param3 = content[i]
        param3 = getPositionOrValue(instruction, param3, 0)
        content[content[i]] = param1 + param2
    elif op == Op.MULTIPLY:
        print(content[i:i+4])
        i += 1
        param1 = content[i]
        param1 = getPositionOrValue(instruction, param1, 2)
        i += 1
        param2 = content[i]
        param2 = getPositionOrValue(instruction, param2, 1)
        i += 1
        param3 = content[i]
        param3 = getPositionOrValue(instruction, param3, 0)
        content[content[i]] = param1 * param2
    elif op == Op.POSITION:
        print(content[i:i+2])
        i += 1
        val = input("Whats the input: ")
        content[content[i]] = int(val)
    elif op == Op.VALUE:
        print(content[i:i+2])
        i += 1
        print(content[content[i]])
    elif op == Op.STOP:
        break
    else:
        break

# print(content)
