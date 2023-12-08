from enum import Enum

class Op(Enum):
    ADD=1
    MULTIPLY=2
    INPUT=3
    OUTPUT=4
    JUMPIFTRUE=5
    JUMPIFFALSE=6
    LESSTHAN=7
    EQUALS=8
    ADJUST=9
    STOP=99

def getInstruction(x):
    string = str(x)
    fivestring = string.zfill(5)
    return Op(int(fivestring[4]))

def getPositionOrValue(instruction, param, position, relativebase, content):
    string = str(instruction)
    fivestring = string.zfill(5)
    posOrVal = fivestring[position]
    if posOrVal == "0":
        return content[param]
    elif posOrVal == "1":
        return param
    else:
        return content[relativebase + param]

def doThirdParameter(instruction, param, position, content):
    string = str(instruction)
    fivestring = string.zfill(5)
    posOrVal = fivestring[position]
    if posOrVal == "0":
        content[content[param]] = param
    else:
        content[param] = param

def intcode(content, inputArr, interactiveMode):
    i = 0
    output = ""
    relativebase = 0
    while True:
        instruction = content[i]
        op = getInstruction(content[i])
        if op == Op.ADD:
            # print(content[i:i+4])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, relativebase, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, relativebase, content)
            i += 1
            param3 = content[i]
            param3 = getPositionOrValue(instruction, param3, 0, relativebase, content)
            content[content[i]] = param1 + param2
            i += 1
        elif op == Op.MULTIPLY:
            # print(content[i:i+4])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, relativebase, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, relativebase, content)
            i += 1
            param3 = content[i]
            param3 = getPositionOrValue(instruction, param3, 0, relativebase, content)
            content[content[i]] = param1 * param2
            i += 1
        elif op == Op.INPUT:
            # print(content[i:i+2])
            i += 1
            if interactiveMode:
                val = input("Whats the input: ")
            else:
                val = inputArr.pop(0)
            # print(val)
            content[content[i]] = int(val)
            i += 1
        elif op == Op.OUTPUT:
            # print(content[i:i+2])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, relativebase, content)
            output += str(param1)
            i += 1
        elif op == Op.JUMPIFTRUE:
            # print(content[i:i+3])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, relativebase, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, relativebase, content)
            if param1 != 0:
                i = param2
            else:
                i += 1
        elif op == Op.JUMPIFFALSE:
            # print(content[i:i+3])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, relativebase, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, relativebase, content)
            if param1 == 0:
                i = param2
            else:
                i += 1
        elif op == Op.LESSTHAN:
            # print(content[i:i+4])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, relativebase, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, relativebase, content)
            i += 1
            param3 = content[i]
            param3 = getPositionOrValue(instruction, param3, 0, relativebase, content)
            if param1 < param2:
                content[content[i]] = 1
            else:
                content[content[i]] = 0
            i += 1
        elif op == Op.EQUALS:
            # print(content[i:i+4])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, relativebase, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, relativebase, content)
            i += 1
            param3 = content[i]
            param3 = getPositionOrValue(instruction, param3, 0, relativebase, content)
            if param1 == param2:
                content[content[i]] = 1
            else:
                content[content[i]] = 0
            i += 1
        elif op == Op.ADJUST:
            i += 1
            param1 = content[i]
            relativebase += param1
            i += 1
        else:
            break
    return output

def part1(filename):
    with open(filename, "r") as f:
        content = list(map(lambda x: int(x), f.readline().split(",")))

    print(intcode(content, [], True))


part1("test.txt")