import time
import random
import functools
from math import ceil

def sort_timer(func):
    """Returns the time needed for a function to operate"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        stop = time.perf_counter()
        result = stop - start
        return result
    return wrapper

@sort_timer
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

def generate_insert_time():
    trial_avgs = []
    tracker = 0
    for x in range(1, 8):
        sort_times = []
        storing_list = []
        # generate random numbers to be stored in list
        for y in range(15*x):
            storing_list.append(random.randint(-10000, 10000))
        # copy randomized list to be insertion-sorted
        for repeat in range(3):
            sort_this = list(storing_list)
            timer = StoogeSort(sort_this)
            sort_times.append(timer)
            print(tracker)
            tracker += 1
        trial_avg = 0
        for trial in range(len(sort_times)):
            trial_avg += sort_times[trial]
        trial_avg /= len(sort_times)
        trial_avgs.append(trial_avg)

        dataOut = open('stoogePlot.txt', 'w')
        dataOut.write(str(trial_avgs))
        dataOut.close()


generate_insert_time()