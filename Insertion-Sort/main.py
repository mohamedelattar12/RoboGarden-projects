def insert_sort(array_of_numbers):

    i = 1
    while i < len(array_of_numbers):
        j = i

        while j > 0 and array_of_numbers[j - 1] > array_of_numbers[j]:
            tmp = array_of_numbers[j - 1]
            array_of_numbers[j - 1] = array_of_numbers[j]
            array_of_numbers[j] = tmp
            j = j - 1

        i = i + 1

    return array_of_numbers

arr =[2,3,4,1,2,66,4,9]
print(insert_sort(arr))