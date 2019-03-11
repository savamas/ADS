def merge_array(array, buffer_array, first_array_begin, first_array_end, second_array_begin, second_array_end):
    # print(array, first_array_begin, first_array_end, second_array_begin, second_array_end)
    sorted_elements_count = 0
    begin = first_array_begin
    end = second_array_end

    inversions_count = 0

    while (first_array_begin <= first_array_end and second_array_begin <= second_array_end):
        if (array[first_array_begin] <= array[second_array_begin]):
            buffer_array[sorted_elements_count] = array[first_array_begin]
            first_array_begin += 1
        else:
            buffer_array[sorted_elements_count] = array[second_array_begin]
            second_array_begin += 1
            inversions_count += first_array_end - first_array_begin + 1
        sorted_elements_count += 1

    for index in range(first_array_begin, first_array_end + 1):
        buffer_array[sorted_elements_count] = array[index]
        sorted_elements_count += 1

    for index in range(second_array_begin, second_array_end + 1):
        buffer_array[sorted_elements_count] = array[index]
        sorted_elements_count += 1

    array[begin:end + 1] = buffer_array[0:sorted_elements_count]

    return inversions_count


def sort_array(array):
    size = len(array)
    buffer_array = [0] * size

    inversions_count = 0
    sorting_size = 2
    while (sorting_size < size * 2):
        first_array_begin = 0
        while (first_array_begin < size):
            second_array_end = first_array_begin + sorting_size - 1

            first_array_end = (first_array_begin + second_array_end) // 2 - (
                        first_array_begin + second_array_end + 1) % 2
            second_array_begin = first_array_end + 1

            if (second_array_begin < size):
                if (second_array_end >= size):
                    second_array_end = size - 1
                inversions_count += merge_array(array, buffer_array, first_array_begin, first_array_end,
                                                second_array_begin, second_array_end)

            first_array_begin += sorting_size
        sorting_size *= 2
    return inversions_count


with open("input.txt", "r") as file_input:
    size = int(file_input.readline())
    array = [int(x) for x in file_input.read().split()]

with open("output.txt", "w") as file_output:
    file_output.write(str(sort_array(array)))