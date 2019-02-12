def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))

'''
5 * fac(4)
    4 * fac(3)
        3 * fac(2)
            2 * fac(1)
                1
            2 * 1
        3 * 2
    4 * 6
5 * 24
=120
'''

# Recursion using lambda
fact = lambda x: 1 if x == 1 else x*fact(x-1)
fact(5)


def sumList(theList):
    if (theList==[]):
        return 0
    else:
        return theList[0] + sumList(theList[1:])

print(sumList([10,20,30,70]))

'''
sum([10,20,30,70])
   a[0] 10 + sum([20,30,70])
       a[0] 20 + sum([30,70])
           a[0] 30 + sum([70])
               a[0] 70 + sum([])
                   0
               70+0=70
           30+70=100
       20+100=120
   10+120=130
result=130
'''

# Recursion using lambda (the condition: <if not theList> equals to <theList==[]> )
sumList = lambda theList: 0 if theList==[] else theList[0] + sumList(theList[1:]) 
sumList([10,20,30,70])

