input = open("input.txt", "r")
output = open("output.txt", "w")

size = input.readline()
array = input.read().split()
result = [int(array[0])]
indicies = [1]

for i in range(1, int(size)):
    for j in range(len(result)):
        if int(array[i]) < result[j]:
            result.insert(j, int(array[i]))
            indicies.append(j + 1)
            break
    else:
        result.append(int(array[i]))
        indicies.append(len(result))

for r in indicies:
    output.write(f"{r} ")
output.write('\n')
for r in result:
    output.write(f"{r} ")