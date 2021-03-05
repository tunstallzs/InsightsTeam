#Dictionaries

#Dictionaries are very similar to Lists in the sense that 
#they store items. The big difference is that they use 
#key values to store information.

#Using our previous example, if we had counties with cases
#we could store them in a dictionary

#Example:
State1 = {'County1' : 1, 'County2' : 2, 'County1' : 3 }
#This is our dictionary. Instead of using index to call 
#variables we use key values for dictionaries.

#If we wanted to know the number for County1, we can get
#this by using
State1['County1']
#this will return the number for County1 which is 1

#If we wanted to change the value of County1 from 1 to 2
#we could do this by
State1['County1'] = 2
#State1 will now look like {'County1' : 2, 'County2' : 2, 'County1' : 3 }

#more python dictionary methods:
#https://www.w3schools.com/python/python_dictionaries_methods.asp