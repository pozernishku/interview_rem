def minimumBribes(q, n):
    bribes = 0
    for i in range(n-1, -1, -1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

q = [3, 1, 5, 4, 2]
n = len(q)
minimumBribes(q, n)