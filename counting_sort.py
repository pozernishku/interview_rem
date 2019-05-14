'''Counting Sort'''
# Require to verify

def counting_sort(arr):
    ar = [0] * 200 # should be 201
    for e in arr:
        ar[e] += 1
    i = 0
    for a in range(200):
        for c in range(ar[a]):
            arr[i] = a
            i += 1
    return arr

counting_sort([2,2,1,1,3,0,199,0])

#[2, 3, 4, 2, 3, 6, 8, 4, 5] 9 5
#[0, 0, 2, 2, 2, 1, 1, 0, 1]
#[2, 2, 3, 3, 4, 6, 8, 4, 5]

