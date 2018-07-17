def binary_sort(a,x):
    left, right = 0, len(a)-1

    while left < right - 1:
        mid = (left + right) // 2
        if a[mid] > x:
            right = mid
        else:
            left = mid
    
    if a[left] == x:
        return a[left]
    else: 
        return -1

print(binary_sort([1,2,3,4,5],3))