import math

with open("./input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

def calcFuel(fuel, totalFuel):
    additionalFuel = math.floor((fuel / 3)) - 2
    if additionalFuel <= 0:
        return totalFuel
    else:
        return calcFuel(additionalFuel, totalFuel + additionalFuel)

content = list(map(lambda x: calcFuel(x, 0), content))

print(sum(content))