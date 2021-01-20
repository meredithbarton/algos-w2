from math import ceil

def StoogeSort(array, left = None , right = None):
    """Sort an array in ascending order"""
    # assign starting values to left and right
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    # n is size of current section of array
    n = right - left + 1
    if n == 2 and array[left] > array[right]:
            # swap
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
    else:
        if n > 2:
            m = ceil(2 * n / 3)
            StoogeSort(array, left, left+m-1)
            StoogeSort(array, right-m+1, right)
            StoogeSort(array, left, left+m-1)
            return array


with open('data.txt', 'r') as read_data:
    data = read_data.read().splitlines()
    all_sorted = []
    # get lines in proper form for sorting
    for elem in data:
        lst = elem.split(" ")
        sort_this = []
        for char in range(0, len(lst)):
            if lst[char] != "":
                # don't add empty spaces to the data set
                sort_this.append(int(lst[char]))
        # sort
        print(sort_this)
        sorted = StoogeSort(sort_this)
        all_sorted.append(sorted)
        print(sorted)
"""
    # write to file
    dataOut = open('stooge.txt', 'w')
    for sorted_list in all_sorted:
        dataOut.write(str(sorted_list))
        dataOut.write("\n")
    dataOut.close()
"""
