import math

with open("./input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

print(content)

content = list(map(lambda x: math.floor((x / 3)) - 2, content))

print(sum(content))