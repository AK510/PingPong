def binarySearch(A, key, n):
    l = 0
    h = int(n-1)
    while(l <= h):
        mid = int((l+h)/2)
        if key == A[mid]:
            return int(mid)
        else:
            if key > A[mid]:
                l = mid + 1
            else:
                h = mid - 1
    return -1


A = [1, 15, 44, 78, 99]
r = binarySearch(A, 78, 5)
print(r)