def add_element(array, n):
    array.append(n)
    middle = (n - 1) // 2
    array[n - 1], array[middle] = array[middle], array[n - 1]

with open('input.txt', 'r') as file_input:
    size = int(file_input.readline())

array = [1, 2]
for ind in range(2, size):
    add_element(array, ind + 1)

with open('output.txt', 'w') as file_output:
    for ind in range(0, min(size, len(array))):
        file_output.write(f'{array[ind]} ')