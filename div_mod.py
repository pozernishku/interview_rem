'''Some of the properties are below
'''

a, b, n = 276, 21, 34
(a + b) % n == (a%n + b%n)%n #True
(a * b) % n == (a%n * b%n)%n #True