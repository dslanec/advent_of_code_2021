f = open("./input", "r")
horizontal = 0
vertical = 0
for line in f:
    instruction = line.split(" ")
    if instruction[0] == "down":
        vertical = vertical + int(instruction[1])
    elif instruction[0] == "up":
        vertical = vertical - int(instruction[1])
    elif instruction[0] == "forward":
        horizontal = horizontal + int(instruction[1])
f.close()
print(horizontal*vertical)