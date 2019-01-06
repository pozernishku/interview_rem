def binary_search(my_list, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if my_list[mid] == x:
            return mid
        elif my_list[mid] > x:
            return binary_search(my_list, l, mid-1, x)
        else:
            return binary_search(my_list, mid+1, r, x)
    else:
        return -1

nums = [2, 3, 4, 10, 40]
x = 10

print(binary_search(nums, 0, len(nums)-1, x))

# def binary_search(a,x):
#     left, right = 0, len(a)-1

#     while left < right - 1:
#         mid = (left + right) // 2
#         if a[mid] > x:
#             right = mid
#         else:
#             left = mid
    
#     if a[left] == x:
#         return a[left]
#     else: 
#         return -1

# print(binary_search([1,2,3,4,5],5))