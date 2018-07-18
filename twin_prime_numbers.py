def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

arr = []
for i in range(0, 15+1):
    if is_prime(i) and is_prime(i+2):
        arr.append((i, i+2))

print(*arr)