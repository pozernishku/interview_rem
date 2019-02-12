'''
Permutations recursively
https://www.youtube.com/watch?v=knByZ7Nh_6o
https://www.youtube.com/watch?v=Jf0WYAbPDKI
'''

def permutations(word):
    if len(word) == 1:
        return [word]
    
    #get all permutations of length N-1
    perms = permutations(word[1:])
    char = word[0]
    result = [] #a list of all permutations of word
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

print(permutations('abc'))


# def permute(nums):
#     return [[nums[i]] + permuted_nums for i in range(len(nums)) for permuted_nums in permute(nums[:i] + nums[i+1:])] or [nums]
# print(permute([1,2,3]))


# perm = lambda nums: [[nums[i]]+perm_nums for i in range(len(nums)) for perm_nums in perm(nums[:i]+nums[i+1:])] or [nums]
# print(perm([1,2,3]))


# def permutations(head, tail=''):
#     n = len(head)
#     if n == 0: 
#         print(tail)
#     else:
#         for i in range(n):
#             permutations(head[:i]+head[i+1:], tail+head[i])
            
# permutations('abc')

# def perm(lst):
#     n = len(lst)
#     if n <= 1:
#         yield lst
#     else:
#         for p in perm(lst[1:]):
#             for i in range(n):
#                 yield p[:i] + lst[0:1] + p[i:]
                
# data = list('abc')
# for p in perm(data):
#     print(p)

# def perm2(elements):
#     n = len(elements)
#     if n <= 1:
#         yield elements
#     else:
#         for perm in perm2(elements[1:]):
#             for i in range(n):
#                 yield perm[:i] + elements[0:1] + perm[i:]

# data = list('abcd')
# for p in perm2(data):
#     print(p)

# def perm1(lst):
#     n = len(lst)
#     if n <= 1:
#         yield lst
#     else:
#         for i in range(n):
#             x = lst[i]
#             xs = lst[:i] + lst[i+1:]
#             for p in perm1(xs):
#                 yield [x]+p
    
# data = list('abc')
# for p in perm1(data):
#     print(p)



# def permutations(iterable, r=None):
#     # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
#     # permutations(range(3)) --> 012 021 102 120 201 210
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = list(range(n))
#     cycles = list(range(n, n-r, -1))
#     yield tuple(pool[i] for i in indices[:r])
#     while n:
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i+1:] + indices[i:i+1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 yield tuple(pool[i] for i in indices[:r])
#                 break
#         else:
#             return

# x = list(permutations('AB'))
# print(x)
# print(len(x))

# from itertools import product
# def permutations(iterable, r=None):
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     for indices in product(range(n), repeat=r):
#         if len(set(indices)) == r:
#             yield tuple(pool[i] for i in indices)

# x = list(permutations('ABC'))
# print(x)
# print(len(x))


# def permutations(head, tail=''):
#     if len(head) == 0: print (tail)
#     else:
#         for i in range(len(head)):
#             permutations(head[0:i] + head[i+1:], tail+head[i])

# x = list(permutations('ABC'))
# print(x, len(x))