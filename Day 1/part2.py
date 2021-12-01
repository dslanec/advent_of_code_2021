f = open("./input", "r")
readings = []
increases = 0
for line in f:
    readings.append(int(line))
f.close()
for index, item in enumerate(readings):
    if index >= 2 and index < len(readings)-1:
        item1 = item + readings[index-1] + readings[index-2]
        item2 = item + readings[index-1] + readings[index+1]
        if item2 > item1:
            increases +=1
print(increases)