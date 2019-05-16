# Complex

import math
import cmath
cmath.sqrt(-5)

c = 3j
c
type(c)
c.real
c.imag
c.real + c.imag*1j
c == c.real + c.imag*1j
c
2+c
x = 2+c
x

x.real
x.imag

arr = [c+3j for c in range(0,4)]
arr = [complex(c,c+5) for c in range(0,4)]
arr
arr[1].real
arr[1].imag
arr[1].imag

my_complex = 2+3j  # (2+3j)
my_complex = complex(2, 3)  # (2+3j)
my_complex

isinstance(my_complex, complex)  # True
my_complex.real
my_complex.imag
my_complex.conjugate()
