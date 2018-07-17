def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    
    result = []
    i, j = 0, 0
    
    #merge the two parts into result[]
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
      
    return result

def merge_sort(list):
    if len(list) < 2:
        return list
  
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)


a = [3,4,5,1,2,8,3,7,6]
# a = [5,7,1,2,3,8,6,5,4]
print(merge_sort(a))