f = open("./input", "r")
readings = []
increases = 0
for line in f:
    readings.append(int(line))
f.close()
for previous, current in zip(readings, readings[1:]):
    if current > previous:
        increases += 1
print(increases)