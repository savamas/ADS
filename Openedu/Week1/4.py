input = open("input.txt", "r")
output = open("output.txt", "w")

size = input.readline()
array = input.read().split()

for ind in range(len(array)):
    array[ind] = [float(array[ind]), ind + 1]
result = [array[0]]

for i in range(1, int(size)):
    for j in range(len(result)):
        if (array[i][0]) < result[j][0]:
            result.insert(j, array[i])
            break
    else:
        result.append(array[i])

output.write(f"{result[0][1]} {result[int(size) // 2][1]} {result[int(size) - 1][1]}")