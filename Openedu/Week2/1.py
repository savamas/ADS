def sort_array(array, output):
    size = len(array)
    buffer_array = [0 for i in range(size)]

    merging_size = 1
    while merging_size < size:
        first_array_begin = 0
        while first_array_begin < size:
            second_array_end = first_array_begin + merging_size * 2 - 1

            first_array_end = (first_array_begin + second_array_end) // 2 - (
                        first_array_begin + second_array_end + 1) % 2
            second_array_begin = first_array_end + 1

            if (second_array_begin < size):
                if (second_array_end >= size):
                    second_array_end = size - 1
                # print(array, buffer_array, first_array_begin, first_array_end, second_array_begin, second_array_end)
                merge_array(array, buffer_array, first_array_begin, first_array_end, second_array_begin,
                            second_array_end)

            first_array_begin += merging_size * 2
        merging_size *= 2
    return


def merge_array(array, buffer_array, first_array_begin, first_array_end, second_array_begin, second_array_end):
    sorted_elements_count = 0
    begin = first_array_begin
    end = second_array_end

    while (first_array_begin <= first_array_end and second_array_begin <= second_array_end):
        if (array[first_array_begin] < array[second_array_begin]):
            buffer_array[sorted_elements_count] = array[first_array_begin]
            first_array_begin += 1
        else:
            buffer_array[sorted_elements_count] = array[second_array_begin]
            second_array_begin += 1
        sorted_elements_count += 1

    for index in range(first_array_begin, first_array_end + 1):
        buffer_array[sorted_elements_count] = array[index]
        sorted_elements_count += 1

    for index in range(second_array_begin, second_array_end + 1):
        buffer_array[sorted_elements_count] = array[index]
        sorted_elements_count += 1

    array[begin:end + 1] = buffer_array[0:sorted_elements_count]

    output.write(f"{begin + 1} {end + 1} {array[begin]} {array[end]}\n")
    return


with open("input.txt", "r") as input:
    size = int(input.readline())
    array = [int(x) for x in input.read().split()]

with open("output.txt", "w") as output:
    sort_array(array, output)
    for element in array:
        output.write(f"{element} ")