import timeit
not_sorted = [1, 123, 32, 654, 23, 765, 3, 23, -3, 5, 12322]
smth = range(100000)
def merge_sort(arr):
    def merge(arr1, arr2):
        arr1.reverse()
        arr2.reverse()
        sorted_arr = []
        for x in range(len(arr1) + len(arr2)):
            l1 = len(arr1) - 1
            l2 = len(arr2) - 1
            if l1 < 0:
                arr2.reverse()
                sorted_arr.extend(arr2)
                break
            elif l2 < 0:
                arr1.reverse()
                sorted_arr.extend(arr1)
                break
            elif arr1[l1] >= arr2[l2]:
                sorted_arr.append(arr1[l1])
                arr1.pop()
            else:
                sorted_arr.append(arr2[l2])
                arr2.pop()
        return sorted_arr
                    
    l = len(arr)
    if l >= 2:
        return merge( merge_sort(arr[:l//2]), merge_sort(arr[l//2:l]) )
    else:
        return arr

print timeit.timeit(lambda: merge_sort(smth), number=1)
