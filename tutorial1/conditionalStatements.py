# If, Else and Elif statements
# What is a conditional statement?
# It tells a program to execute different actions depending on whether the condition is true or false

#Background

#Boolean value: a value that is either true or false
    # x > 4
    # X> y
    # z = (1+x)

#Logical Oporators: and, or, and not

##'If' Statement: Prints results when one of the conditions is true or false
if <expr>:
    <statement>

#Create a compound statement or block. Blocks are defined by indentation.
if <expr>:
    <statement>
    <statemet>
    ...
    <statement>
<following_statement>

#Note: the equality sign means 'to assign a value' 
#To check if a condition is satisfied, we use use the doubl equality sign (==)

##'ELSE' Statement: prints statement when one condition fails to meet the requirement
if <expr>:
    <statement(s)>  #executed if condition evaluates to True
else:
    <statement(s)>  #executed if condition evaluates to False

#Note: Remember that indentation plays a key role and defines blocks.
#The 'if' and 'else' statements must be on the same vertical line.

##'ELIF' Statement: used when the third possibility has an the outcome.
if x < y:
    Statements_a
elif x > y:
    Statments_b
else:
    Statements_c

#Note: 'ELSE' clause is optional, but if included, there can only be one and it must be last. 

##For more information and visuals, there are good site:
#https://openbookproject.net/thinkcs/python/english3e/conditionals.html 
#https://realpython.com/python-conditional-statements/
