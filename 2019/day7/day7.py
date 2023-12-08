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
    STOP=9

def getInstruction(x):
    string = str(x)
    fivestring = string.zfill(5)
    return Op(int(fivestring[4]))

def getPositionOrValue(instruction, param, position, content):
    string = str(instruction)
    fivestring = string.zfill(5)
    posOrVal = fivestring[position]
    if posOrVal == "0":
        return content[param]
    else:
        return param

def doThirdParameter(instruction, param, position, content):
    string = str(instruction)
    fivestring = string.zfill(5)
    posOrVal = fivestring[position]
    if posOrVal == "0":
        content[content[param]] = param
    else:
        content[param] = param

def intcode(content, inputArr):
    i = 0
    output = ""
    while True:
        instruction = content[i]
        op = getInstruction(content[i])
        if op == Op.ADD:
            # print(content[i:i+4])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, content)
            i += 1
            param3 = content[i]
            param3 = getPositionOrValue(instruction, param3, 0, content)
            content[content[i]] = param1 + param2
            i += 1
        elif op == Op.MULTIPLY:
            # print(content[i:i+4])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, content)
            i += 1
            param3 = content[i]
            param3 = getPositionOrValue(instruction, param3, 0, content)
            content[content[i]] = param1 * param2
            i += 1
        elif op == Op.INPUT:
            # print(content[i:i+2])
            i += 1
            val = inputArr.pop(0)
            # print(val)
            content[content[i]] = int(val)
            i += 1
        elif op == Op.OUTPUT:
            # print(content[i:i+2])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, content)
            output += str(param1)
            i += 1
        elif op == Op.JUMPIFTRUE:
            # print(content[i:i+3])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, content)
            if param1 != 0:
                i = param2
            else:
                i += 1
        elif op == Op.JUMPIFFALSE:
            # print(content[i:i+3])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, content)
            if param1 == 0:
                i = param2
            else:
                i += 1
        elif op == Op.LESSTHAN:
            # print(content[i:i+4])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, content)
            i += 1
            param3 = content[i]
            param3 = getPositionOrValue(instruction, param3, 0, content)
            if param1 < param2:
                content[content[i]] = 1
            else:
                content[content[i]] = 0
            i += 1
        elif op == Op.EQUALS:
            # print(content[i:i+4])
            i += 1
            param1 = content[i]
            param1 = getPositionOrValue(instruction, param1, 2, content)
            i += 1
            param2 = content[i]
            param2 = getPositionOrValue(instruction, param2, 1, content)
            i += 1
            param3 = content[i]
            param3 = getPositionOrValue(instruction, param3, 0, content)
            if param1 == param2:
                content[content[i]] = 1
            else:
                content[content[i]] = 0
            i += 1
        else:
            break
    return output

def calculate(inputs, filename):
    output = ""
    valueFromPrevRun = 0
    for inp in inputs:
        # reset content
        with open(filename, "r") as f:
            content = list(map(lambda x: int(x), f.readline().split(",")))
        valueFromPrevRun = int(intcode(content, [inp, valueFromPrevRun]))
        output = str(valueFromPrevRun)
    return output


def part1(filename):
    max = 0
    for i1 in range(5):
        for i2 in range(5):
            if i2 == i1:
                continue
            for i3 in range(5):
                if i3 == i2 or i3 == i1:
                    continue
                for i4 in range(5):
                    if i4 == i3 or i4 == i2 or i4 == i1:
                        continue
                    for i5 in range(5):
                        if i5 == i4 or i5 == i3 or i5 == i2 or i5 == i1:
                            continue
                        # print(i1, i2, i3, i4, i5)
                        val = int(calculate([i1, i2, i3, i4, i5], filename))
                        if val > max:
                            max = val

    print("max", max)


part1("input.txt")
