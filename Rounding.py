# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../../../var/folders/xr/jv5nzs9972zcwf_kryyqtdkw0000gn/T'))
	print(os.getcwd())
except:
	pass
#%%
#!/usr/bin/env bash

#%% [markdown]
# https://realpython.com/python-rounding/#truncation

#%%
# The “rounding half to even strategy” 
# is the strategy used by Python’s built-in round() function 
# and is the default rounding rule in the IEEE-754 standard.


#%%
round(2.5)


#%%
round(1.5)


#%%
round(3.5)


#%%
round(4.5)


#%%
0.1 + 0.1 + 0.1 # machine storage precision error


#%%



#%%
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


#%%
truncate(0.031286, 3) # decimals accepts even negatives: truncate(12.1286, -1) or truncate(-1374.25, -1)


#%%



#%%
import random
random.seed(100) # to get the same results as before
actual_value, truncated_value = 100, 100

for _ in range(1000000):
    randn = random.uniform(-0.05, 0.05)
    actual_value = actual_value + randn
    truncated_value = truncate(truncated_value + randn, 3)


#%%
actual_value


#%%
truncated_value


#%%



#%%
import random
random.seed(100) # to get the same results as before
actual_value, rounded_value = 100, 100

for _ in range(1000000):
    randn = random.uniform(-0.05, 0.05)
    actual_value = actual_value + randn
    rounded_value = round(rounded_value + randn, 3)


#%%
actual_value


#%%
rounded_value


#%%



#%%
import math
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


#%%
round_up(10.26745, 2) # Just like truncate(), you can pass a negative value to decimals: round_up(1352, -2)


#%%



#%%
import math
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


#%%
round_down(10.26745, 2) # round_down(-0.5)


#%%


#%% [markdown]
# Interlude: Rounding Bias: https://realpython.com/python-rounding/#interlude-rounding-bias

#%%
data = [1.25, -2.67, 0.43, -1.79, 4.32, -8.19]


#%%
import statistics


#%%
statistics.mean(data)


#%%
ru_data = [round_up(n, 1) for n in data]


#%%
ru_data


#%%
statistics.mean(ru_data)


#%%



#%%
rd_data = [round_down(n, 1) for n in data]


#%%
rd_data


#%%
statistics.mean(rd_data)


#%%



#%%
tr_data = [truncate(n, 1) for n in data]


#%%
tr_data


#%%
statistics.mean(tr_data)


#%%


#%% [markdown]
# What about the number 1.25? You probably immediately think to round this to 1.3, but in reality, 1.25 is equidistant from 1.2 and 1.3. In a sense, 1.2 and 1.3 are both the nearest numbers to 1.25 with single decimal place precision. The number 1.25 is called a **tie** with respect to 1.2 and 1.3. In cases like this, you must assign a tiebreaker.
# 
# The way that most people are taught break ties is by rounding to the greater of the two possible numbers.

#%%
1.20
1.21
1.22
1.23
1.24

1.25 # tie

1.26
1.27
1.28
1.29
1.30


#%%



#%%
import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


#%%
round_half_up(1.25, 1)


#%%
round_half_up(-1.5)


#%%
round_half_up(-1.25, 1)


#%%
round_half_up(2.5)


#%%
round_half_up(-1.225, 2) # Look here


#%%
-1.225 * 100 # This is why


#%%



#%%
# Error (check and try to solve or just use Decimal module)
def round_half_up(n, decimals=0):
    k = 15 # extreme big power
    multiplier = 10 ** k
    return (n*multiplier + (0.5*10**(k-decimals))) / multiplier


#%%
round_half_up(-1.225, 2) # And then look here


#%%
round_half_up(-1.2252, 2) # Error (check and try to solve or just use Decimal module)


#%%



#%%
import math
def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier - 0.5) / multiplier


#%%
round_half_down(1.5)


#%%
round_half_down(-1.5)


#%%
round_half_down(2.25, 1)


#%%
data = [-2.15, 1.45, 4.35, -12.75]


#%%
import statistics
statistics.mean(data)


#%%
rhu_data = [round_half_up(n, 1) for n in data]
statistics.mean(rhu_data)


#%%
rhd_data = [round_half_down(n, 1) for n in data]
statistics.mean(rhd_data)


#%%
# Error (check and try to solve or just use Decimal module)
def round_half_down(n, decimals=0):
    k = 15 # extreme big power
    multiplier = 10 ** k
    return (n*multiplier - (0.5*10**(k-decimals))) / multiplier


#%%
round_half_down(2.252, 2) # Error (check and try to solve or just use Decimal module)


#%%
# if n >= 0:
#     rounded = round_half_up(n, decimals)
# else:
#     rounded = round_half_down(n, decimals)


#%%
import math
def round_half_away_from_zero(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)


#%%
round_half_away_from_zero(12.25, 0)


#%%
round_half_away_from_zero(1.5)


#%%
round_half_away_from_zero(-1.5)


#%%
round_half_away_from_zero(-12.75, 1)


#%%



#%%
data = [-2.15, 1.45, 4.35, -12.75]


#%%
import statistics
statistics.mean(data)


#%%
rhaz_data = [round_half_away_from_zero(n, 1) for n in data]


#%%
statistics.mean(rhaz_data)


#%%


#%% [markdown]
# The “rounding half to even strategy” is the strategy used by Python’s built-in round() function and is the default rounding rule in the IEEE-754 standard. 
# https://en.wikipedia.org/wiki/IEEE_754#Rounding_rules

#%%
round(4.5)


#%%
round(3.5)


#%%
round(1.75, 1)


#%%
round(1.65, 1)


#%%
round(2.675, 2) # round() suffers from the same error in round_half_up() due floating-point representation error.


#%%



#%%
# Floating-point representation errors:


#%%
round(1.165, 2) # Expected value: 1.16


#%%
round(1.275, 2) # Expected value: 1.28


#%%
round(2.675, 2) # Expected value: 2.68


#%%
round(-1.225, 2) # Expected value: -1.22


#%%



#%%
import decimal


#%%
# Default ROUND_HALF_EVEN strategy
decimal.getcontext()


#%%
from decimal import Decimal


#%%
Decimal("0.1")


#%%
Decimal(0.1) # floating-point representation error if arg is not str.


#%%
Decimal('0.1') + Decimal('0.1') + Decimal('0.1')


#%%
# Compare to
0.1 + 0.1 + 0.1


#%%
Decimal("1.65").quantize(Decimal("1.0")) # number of decimal places to round the number. Ex: 1.00, 1.000 etc


#%%



#%%
Decimal("1.165").quantize(Decimal("1.00")) # rounding to 2 dec places - fixed


#%%
Decimal("1.275").quantize(Decimal("1.00")) # rounding to 2 dec places - fixed


#%%
Decimal("2.675").quantize(Decimal("1.00")) # rounding to 2 dec places - fixed


#%%
Decimal("-1.225").quantize(Decimal("1.00")) # rounding to 2 dec places - fixed


#%%



#%%
# Look how half to even rounding works on long floats.


#%%
Decimal("17.92857142857143").quantize(Decimal("1.000"))


#%%
Decimal("9.1285000001").quantize(Decimal("1.000"))


#%%
Decimal("9.128500000").quantize(Decimal("1.000"))


#%%
Decimal("9.1285").quantize(Decimal("1.000"))


#%%


#%% [markdown]
# Another benefit of the decimal module is that rounding after performing arithmetic is taken care of automatically, and significant digits are preserved. To see this in action, let’s change the default precision from twenty-eight digits to two, and then add the numbers 1.23 and 2.32:

#%%
decimal.getcontext().prec = 2
Decimal("1.23") + Decimal("2.32")


#%%



#%%
decimal.getcontext().rounding = decimal.ROUND_CEILING # round_up()
Decimal("1.32").quantize(Decimal("1.0"))


#%%
decimal.getcontext().rounding = decimal.ROUND_CEILING # round_up()
Decimal("-1.32").quantize(Decimal("1.0"))


#%%



#%%
decimal.getcontext().rounding = decimal.ROUND_FLOOR # round_down()
Decimal("1.32").quantize(Decimal("1.0"))


#%%
decimal.getcontext().rounding = decimal.ROUND_FLOOR # round_down()
Decimal("-1.32").quantize(Decimal("1.0"))


#%%



#%%
decimal.getcontext().rounding = decimal.ROUND_DOWN # truncate() (towards zero)
Decimal("1.32").quantize(Decimal("1.0"))


#%%
decimal.getcontext().rounding = decimal.ROUND_DOWN # truncate() (towards zero)
Decimal("-1.32").quantize(Decimal("1.0"))


#%%



#%%
decimal.getcontext().rounding = decimal.ROUND_UP # not_implemented() (away from zero)
Decimal("1.32").quantize(Decimal("1.0"))


#%%
decimal.getcontext().rounding = decimal.ROUND_UP # not_implemented() (away from zero)
Decimal("-1.32").quantize(Decimal("1.0"))


#%%



#%%
decimal.getcontext().rounding = decimal.ROUND_HALF_UP # round_half_away_from_zero
Decimal("1.35").quantize(Decimal("1.0"))


#%%
decimal.getcontext().rounding = decimal.ROUND_HALF_UP # round_half_away_from_zero
Decimal("-1.35").quantize(Decimal("1.0"))


#%%



#%%
decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN # not_implemented(). Breaks ties by rounding towards zero
Decimal("1.35").quantize(Decimal("1.0")) # round half truncate


#%%
decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN # not_implemented(). Breaks ties by rounding towards zero
Decimal("-1.35").quantize(Decimal("1.0")) # round half truncate


#%%



#%%
# These two rounding strategies I've not found in decimal module


#%%
round_half_down(1.35,1)


#%%
round_half_down(-1.35,1)


#%%
round_half_up(1.35,1)


#%%
round_half_up(-1.35,1)


#%%


#%% [markdown]
# The final rounding strategy available in the decimal module is very different from anything we have seen so far:

#%%
decimal.getcontext().rounding = decimal.ROUND_05UP
Decimal("1.38").quantize(Decimal("1.0"))


#%%
decimal.getcontext().rounding = decimal.ROUND_05UP
Decimal("1.35").quantize(Decimal("1.0"))


#%%
decimal.getcontext().rounding = decimal.ROUND_05UP
Decimal("-1.35").quantize(Decimal("1.0"))


#%%



#%%
# Explanation

#%% [markdown]
# In the first example, the number 1.49 is first rounded towards zero in the second decimal place, producing 1.4. Since 1.4 does not end in a 0 or a 5, it is left as is. On the other hand, 1.51 is rounded towards zero in the second decimal place, resulting in the number 1.5. This ends in a 5, so the first decimal place is then rounded away from zero to 1.6.

#%%
Decimal("1.49").quantize(Decimal("1.0"))


#%%
Decimal("1.51").quantize(Decimal("1.0"))


#%%



#%%
# Total

# Rounding Up +     round_up()     decimal.ROUND_CEILING
# Rounding Down +   round_down()   decimal.ROUND_FLOOR
# Truncation +      truncate()     decimal.ROUND_DOWN    (towards zero)
# Rounding Half Up -  not_implemented()    ?? not found in decimal module
# Rounding Half Down - not_implemented()   ?? not found in decimal module
# Rounding Half Away From Zero +   round_half_away_from_zero()  decimal.ROUND_HALF_UP
# Rounding Half To Even +  round()  decimal.ROUND_HALF_EVEN    (default in Decimal module)
# decimal.ROUND_05UP - not_implemented()   in decimal module


#%%


#%% [markdown]
# General: https://en.wikipedia.org/wiki/Rounding
#%% [markdown]
# Excellent in python:
# https://realpython.com/python-rounding/#truncation
#%% [markdown]
# bash bc: https://unix.stackexchange.com/questions/167058/how-to-round-floating-point-numbers-in-shell
#%% [markdown]
# Bellow is an example task based on rounding manipulation.

#%%
'''A vending machine has the following denominations: 1c, 5c, 10c, 25c, 50c, and $1. 
Your task is to write a program that will be used in a vending machine to return change. 
Assume that the vending machine will always want to return the least number of coins or notes. 
Devise a function getChange(M, P) 
where M is how much money was inserted into the machine and P the price of the item selected, 
that returns an array of integers representing the number of each denomination to return. 

Example:
getChange(5, 0.99) // should return [1,0,0,0,0,4]
https://docs.python.org/3/tutorial/floatingpoint.html
'''

# Complete
# https://docs.python.org/3/tutorial/floatingpoint.html
def getChange(M, P):
    a = [0, 0, 0, 0, 0, 0]
    b = [100, 50, 25, 10, 5, 1]
    M *= 100
    P = round(P*100) # This is very important
    r = M - P
    
    print(M, P, r)
    for i, v in enumerate(b):
        a[i] = r//v
        r %= v
        
    return a[::-1]

getChange(5, 3.15)


# Some interesting examples
4.1 * 100
0.99 * 100
round(4.1*100)
format(4.1*100, '.0f')
round(0.99 * 100)
format(0.99 * 100, '.0f')


#%%


