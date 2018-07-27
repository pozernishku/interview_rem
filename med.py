def med(arz, d):
    if d%2!=0:
        d = -(-d // 2)
        for i in range(len(arz)):
            d = d - arz[i]
            if d <= 0: return i
    elif d%2==0:
        d = -(-d // 2)
        m1 = d
        m2 = d + 1
        for i in range(len(arz)):
            m1 = m1 - arz[i]
            if m1 <= 0: 
                m1 = i
                break
        for i in range(len(arz)):
            m2 = m2 - arz[i]
            if m2 <= 0:
                m2 = i
                break
                
        return (m1+m2)/2

def activityNotifications(arr, n, d):
    nf, m = 0, 0
    
    b = arr[d:]
    c = arr[:-d]
    g = arr[:d]
    bc = zip(b,c)
    
    a = [0] * 200
    for e in g:
        a[e] += 1
    
    for i,j in bc:
        m = med(a,d)
        a[i] += 1
        a[j] -= 1
        if i >= 2*m:
            nf += 1
            
    return nf


print(activityNotifications([1,2,3,4,4], 5, 4))
med([0,3,2,1,1,1],8)