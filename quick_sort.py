import random

def quick_sort(s):
    if len(s) > 1:
        pivot = random.choice(s)

        less = [x for x in s if x < pivot]
        greater = [x for x in s if x > pivot]
        equal = [x for x in s if x == pivot]

        return quick_sort(less) + equal + quick_sort(greater)
    else: return s

a = [2,1,5,0,1,5,7,14,-4]
print(quick_sort(a))
