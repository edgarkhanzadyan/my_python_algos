import timeit
not_sorted = [1, 123, 32, 654, 23, 765, 3, 23, -3, 5, 12322]
big = range(10000)
def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
    return arr

def insertion_sort (arr):
    arr_len = len(arr)
    for x in range(arr_len):
        for y in range(x, -1, -1):
            if not y == 0 and arr[y] > arr[y-1]:
                arr = swap(arr, y, y-1)
    return arr

def insertion_sort_binary (arr):
    def sort(small_arr, val, count):
        l = len(small_arr)
        if l <= 1:
            if not l == 0 and val < small_arr[0]:
                return count + 1
            else:
                return count
        if val > small_arr[l // 2]:
            return sort(small_arr[:l // 2], val, count)
        else:
            return sort(small_arr[l // 2: l], val, count + l // 2)
    arr_len = len(arr)
    for x in range(arr_len-1):
        k = sort(arr[:x+1], arr[x+1], 0)
        arr.insert(k, arr[x + 1])
        arr.pop(x + 2)
    return arr
print timeit.timeit(lambda: insertion_sort(big), number=1)
print timeit.timeit(lambda: insertion_sort_binary(big), number=1)
