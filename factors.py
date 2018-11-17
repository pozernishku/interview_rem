'''
Largest prime factor
https://projecteuler.net/problem=3
'''
# Done from pseudo code in PDF
n = 600851475143222222
if n%2 == 0:
    lastFactor = 2
    n=n//2
    while n%2==0:
        n=n//2
else:
    lastFactor = 1
factor = 3

maxFactor = n**0.5

while n>1 and factor <= maxFactor:
    if n%factor==0:
        n=n//factor
        lastFactor=factor
        while n%factor == 0:
            n=n//factor
        maxFactor=n**0.5
    factor += 2
if n == 1:
    print(lastFactor)
else:
    print(n)