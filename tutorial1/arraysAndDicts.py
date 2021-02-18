# Arrays and Dictonaries 

#Arrays and Dictionaries are both great ways to
#store information using one variable on python

#List:

#Example 1)
#Suppose we have three counties in State1:
#Instead of storing each county name in
#separate variables we can store the county names
#into one list variable

State1 = ["County1", "County2", "County3"]

#Accessing list variables:

#For whatever variable in the list we want to access,
#we are able to call it using its list index.
#The index for a list starts at 0 and ends at the
#length of the list - 1

#in our previous example:

State1 = ["County1", "County2", "County3"]
#index:      0          1           2

#If we wanted to access County1 we would call it by
#using the braces with the list index
#For instance: "County1" would be State1[0]
#              "County2" would be State1[1]
#              "County2" would be State1[2]

State1[0:2]
#This index tells us that we want to take 2 items from
#State1 starting from State1[0]
#Therefore this reurns ['County1', 'County2']
#List operations:

#If we wanted to change a list item. Suppose we
#wanted to change "County3" to "County4" we would
#do this by setting State1[2]  equal to "County4"
State1[2] = "County4"

#now
#State1 is equal to ["County1", "County2", "County4"]

#add to list
#To add to list we can use the append function

State1.append("County3")

#this will add County3 to the end of the list
#State1 is equal to ["County1", "County2", "County4", "County3"]

#sorting list:
#a quick way to sort the list is by using the sort() method
State1.sort()
#State1 is equal to ['County1', 'County2', 'County3', 'County4']

#remove/pop item:
#remove item works slightly differently in that you give
#the remove function the item you want to remove from the list
State1.remove("County4")
#State1 is equal to ["County1", "County2", "County3"]
State1.append("County4")
#If we wanted to remove the last item of the list and 
#we knew that our last list index was 3, we could use the pop
#function
State1.pop(3)
#State1 is equal to ["County1", "County2", "County3"]

#Suppose
#State1 is equal to ["County1", "County2", "County3", "County2"]
#remove("County2") will remove the first(left-most) instance of County2
State1 = ["County1", "County2", "County3", "County2"]
State1.remove("County2")
#State1 is now equal to ['County1', 'County3', 'County2']

#List indexing:
#Suppose n is a number from 1 to our list size

#State1[n:] returns a list of every item in State1
#after the first n entries
State1.sort()
#State1 = ["County1", "County2", "County3"]
State1[1:]
#this returns ['County2', 'County3']

#State1[:n] returns a list of the first n items
#in State1
State1[:1]
#this returns ['County1']
State1[:2]
#this returns ['County1', 'County2']

#State1[-n:] returns the last n items in State1
State1[-1:]
#this returns ['County3']
State1[-2:]
#this returns ['County2', 'County3']

#State1[:-n] returns every item in State1 before
#the last n items
State1[:-1]
#this returns ['County1', 'County2']
State1[:-2]
#this returns ['County1']

#other methods can be found here
#https://www.w3schools.com/python/python_lists_methods.asp

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