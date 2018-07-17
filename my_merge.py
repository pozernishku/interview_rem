def merge(left, right):
    # some condition checking

    i, j = 0, 0
    res = []

    while len(res) < len(left) + len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        
        if i == len(left) or j == len(right):
            res.extend(left[i:] or right[j:])
            break

    return res

def merge_sort(list):
    if len(list) < 2:
        return list

    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left,right)

x = [3,2,1,2,3,4,1]
print(merge_sort(x))