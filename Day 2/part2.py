f = open("./input", "r")
horizontal = 0
vertical = 0
aim = 0
for line in f:
    instruction = line.split(" ")
    if instruction[0] == "down":
        aim = aim + int(instruction[1])
    elif instruction[0] == "up":
        aim = aim - int(instruction[1])
    elif instruction[0] == "forward":
        horizontal = horizontal + int(instruction[1])
        vertical = vertical + (aim * int(instruction[1]))
f.close()
print(horizontal*vertical)