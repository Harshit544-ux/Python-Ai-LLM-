# Integer
print(42)

# Decimal/Float
print(3.14)

# Boolean - True or False
print(True)
print(False)

# String 
# In Python, there is no separate character type;
# even a single letter is treated as a string
print("Hello, World!")
print('A')  # This is a string, not a character


# complex
print(2+3j)


# List - C language -> Array 
list =[1,2,3,4,5,6]
print(list)

# Tuple 
tuple = [(1,2,3,4,5,6)]
print(tuple)

#  Dictionary ;- { key : value_pairs }
dict = {"name":"Harshit","age":22,"city":"Hyderabad"}
print(dict)


# sets
set = {1,2,3,4,5,}
print(set)


# type() - is a function which are used to find the data type of the variable or value
print(type(4))
print(type([1,2,3,4]))
print(type((1,2,3,4)))
print(type({"name":"Harshit","age":22}))
print(type({1,2,3,4}))


# === Variables === 
#  A variables is just like a container which is used to store the data or value.
#  In Python, we don't need to declare the variable with a specific data type, it will automatically detect the data type of the variable based on the value assigned to it.

# so basically other language like c , c++ , java need to declare the data type of variable
# eg :- int name = "Harshit" 

# in python we can directly assign the value to the variable without need data type declare
name = "Harshit"
print(name)

a = 5
b = 6
c = a+b
print(c)


# Dynamic typing - is it a way in which , we don't tell a data type of a variable
a = 5

# Static typing - is it a way in which , we need to tell a data type of a variable
# int a = 5


# Dynamic binding - (python)
a = 5 
print(a)
a = "Harshit"
print(a)

# Static binding - (c,c++)
# int a = 5;
# a = "Harshit"; // error because we can't change the data type of variable in static binding language


# === Traditional way ===
a = 5 
b = 6
c = 8 
print (a,b,c)

# Another way to write the variable
a,b,c = 5,6,8
print(a,b,c)
 
#  if you want to assign the same value to multiple variables
a = b = c = 5
print(a,b,c)


# keywords - in python they are 32 keywords 
# keywords - eg :- True . False , if , else , elif , for , while , break , continue , pass , def , return , import , from , as , class , try , except , finally , raise , with , lambda , nonlocal , global , assert, yield, del, in, is, not, or, and etc
# Basically keywords are understand by the python  interpreter 


# Identifiers - is the name which we give to the variable , function , class etc
# Rules for naming identifiers in python
# 1) You can't start with a digit
#  eg :- 1name = "Harshit" // it throw an error
# 2) You can use special characters -> _ (underscore)
# eg :- _name = "Harshit" // it is valid
_= "Harshit"
print(_)
# 3) Identifiers are not be keywords
# eg :- True = "Harshit" // it throw an error because True is a keyword