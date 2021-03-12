# Data Types 

# Here we assign the int (integer) 2021 to the variable num 
# We can check the type by using the function type()
num = 2021     
print("num: ", num, "\nnum data type: ", type(num), "\n")  


# Floats (decimals)
flt = 2020.2
print("flt: ", flt, "\nflt data type:", type(flt), "\n")

# Strings (text!)
string = "Part II num float whatever"
print(f"string: {string}\nstring data type: {type(string)}\n")

# Boolean (true and false)
boolean = True
print(f"boolean: {boolean}\nboolean data type: {type(boolean)}\n")

# How do we convert between the different types?
# We can use type casting! 
string = str(num) 
print(f"string: {string}, num: {num}")                  # Note that num does not change! 
print(f"bool(0) --> {bool(0)}, bool(1) --> {bool(1)}")  # boolean is kind of special in Python! 
print(f"bool(\"\") --> {bool('')}, , bool(\"hello!\") --> {bool('Hello')}")
print("String in Python can be 'falsy', which can be useful in many circumstances!\n")

# Variables and Assingments 
# So far, when we do x = 5, we assign 5 to the variable 5
# We can then reuse x as much as we like! 
x = 5
print("x: ", x)
print("x * 5: ", x * 5, "\n")


# If we want to change the value of x, we need to reassign something to it! 
x = x * 2
print("After x = 10: x = ", x, "\n")

# We can perform normal arithmetic on x as asual
x = x + 5
print("After x = x + 5: x =", x)
x = x - 5 
print("After x = x - 5: x =", x)
x = x * 10
print("After x = x * 5: x =", x)
x = x / 10 
print("After x = x / 5: x =", x, "\n")

# To make this much faster (because we're lazy), we can use 
# special operators! 
x += 5                          # this is the same as x = x + 5
x -= 5                          # this is the same as x = x - 5
x *= 5                          # this is the same as x = x * 5
x /= 5                          # this is the same as x = x / 5 
