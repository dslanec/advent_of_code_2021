f = open("./input", "r")
readings = []
increases = 0
for line in f:
    readings.append(line)
f.close()

gamma = []
epsilon = []

for i in range(12):
    count = 0
    for x in readings:
        if int(x[i]) == 1:
            count += 1
    if count > 500:
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")
gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)
print(gamma * epsilon)
