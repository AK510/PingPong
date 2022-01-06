def rBinarySearch(A, l, h, key):
    if l <= h:
        mid = int((l+h)/2)
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            return rBinarySearch(A, mid+1, h, key)
        else:
            return rBinarySearch(A, l, mid-1, key)
    return -1


A = [1, 15, 44, 78, 99]
r = rBinarySearch(A, 0, 5, 78)
print(r)
