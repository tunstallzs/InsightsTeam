#A loop is a tool in programming that we can use to repeat 
# a certain set of instructions until a certain criteria is
#met.

#While loop 

#A while loop in python runs until the loop criteria is false
#ex1:
n = 1
while(n <= 5):
    print(n)
    n += 1

#Output:
#1
#2
#3
#4

#This loop prints ut every number from 1 to 5

#Looping through a list using a while loop
#For loop

#Suppose we had a list 
State1 = [1,3,4,5,3,4,6]
i = 0
while(i < len(State1)):
    print(State1[i])
    i += 1

#Output:
#1
#3
#4
#5
#3
#4
#6

#For loop

#for loops loop through values from start to finish from an object
for i in State1:
    print(i)

#Output:
#1
#3
#4
#5
#3
#4
#6

#Looping through a dictionary using a for loop:

stateDict = {'a':1,'b':3,'c':4,'d':5,'e':3,'f':4,'g':6}
for i in stateDict:
    print(stateDict[i])

#Output:
#1
#3
#4
#5
#3
#4
#6