def merge(left, right):
    array = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))
 
        if len(left) != 0:
            array.extend(left)
        elif len(right) != 0:
            array.extend(right)

        return array

def merge_sort(array):
    if len(array) < 2:
        return array
 
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

x = [2,1,5,3,8,6]
print(merge_sort(x))