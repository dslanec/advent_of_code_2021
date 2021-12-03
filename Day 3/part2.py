f = open("./input", "r")
readings = []
increases = 0
for line in f:
    readings.append(line)
f.close()

def array_filter(array, index, keep):
    if len(array) ==1:
        return array
    tmp = []
    for x in array:
        if x[index] == keep:
            tmp.append(x)
    return tmp

def count(array, index, type):
    count = 0
    for x in array:
        if int(x[index]) == 1:
            count += 1
    if count/len(array) >= 0.5 and type == 'o':
            return "1"
    elif count/len(array) >= 0.5 and type == 'c':
        return "0"
    elif count/len(array) < 0.5 and type == 'o':
        return "0"
    else:
        return "1"


oxygen = readings
co2 = readings

for i in range(12):
    oxygen = array_filter(oxygen, i, count(oxygen, i, "o"))
    co2 = array_filter(co2, i, count(co2, i, "c"))
print(int(''.join(oxygen), 2) * int(''.join(co2), 2))
