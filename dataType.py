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