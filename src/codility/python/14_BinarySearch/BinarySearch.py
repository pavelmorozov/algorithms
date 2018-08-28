def binarySearch(A, x):
    n = len(A)
    beg = 0
    end = n - 1
    result = -1
    while (beg <= end):
        mid = (beg + end) // 2
        if (A[mid] <= x):
            beg = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

A = [1,3,7,9,12,18,23,24,25,27,29,31]
print(binarySearch(A, 17))
print(binarySearch(A, 18))
print(binarySearch(A, 23))