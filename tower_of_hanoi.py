#// Created by Varshini Siva

#The tower of hanoi is very simple in python 
#It is possible only because of the recursive function
#It contains three rods and n number of disca
#The rules of tower of hanoi puzzles are  1.Only one disc is allowed to move at a time.  2.Only the top disc of the rod can be moved from one rod to another  3.Only the smaller disc can be placed above the larger one
#The number of moves is calculated using the formula 2^n-1
#Give the number of discs 'n' as the input
def th(n,s,t,a):
	if(n==1):
		print("move",n,"from",s,"to",t)
	else:
		th(n-1,s,a,t)
		print("move",n,"from",s,"to",t)
		th(n-1,a,t,s)
number=int(input()) #enter the number of discs
source=1 #represents the starting rod number
target=3 #represents the ending rod number
auxillary=2 #represents the middle rod number
th(number,source,target,auxillary)