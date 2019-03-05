input = open("input.txt", "r")
output = open("output.txt", "w")

size = input.readline()
array = [int(x) for x in input.read().split()]

for i in range(len(array)):
    min_element_index = i
    for j in range(i + 1, len(array)):
        if array[min_element_index] > array[j]:
            min_element_index = j
    if min_element_index != i:
        array[i], array[min_element_index] = array[min_element_index], array[i]
        output.write(f'Swap elements at indices {i + 1} and {min_element_index + 1}.\n')

output.write('No more swaps needed.\n')
for element in array:
    output.write(f'{element} ')