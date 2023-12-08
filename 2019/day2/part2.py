with open("input.txt", "r") as f:
    content = list(map(lambda x: int(x), f.readline().split(",")))

def operateTwoValues(x, one, two):
    if x == 1:
        return one + two
    elif x == 2:
        return one * two
    else:
        return None

for x1 in range(100):
    for x2 in range(100):
        content2 = [x for x in content]
        content2[1] = x1
        content2[2] = x2
        # print(content2)
        for i in range(0, len(content2), 4):
            intcode = content2[i:i+4]
            if intcode[0] == 99:
                break
            toAppend = operateTwoValues(intcode[0], content2[intcode[1]], content2[intcode[2]])
            if toAppend == None:
                break
            content2[intcode[3]] = toAppend
        if content2[0] == 19690720:
            print(x1, x2)