def selection_sort(arr):
    length = len(arr)
    for start_index in range(length):
        smallest_index = start_index
        for index in range(start_index + 1, length):
            if arr[index] < arr[smallest_index]:
                smallest_index = index
        arr[start_index], arr[smallest_index] = arr[smallest_index], arr[start_index]
    return arr
