# Operators
# Arithmetic Operators
# Relational Operators
# Logical Operators
# Assignment Operators
# Membership Operators

# ====== Arithmetic Operators ====== 
print(5+3)

print(5-3)

print(5*3)

print(5/3)
 
print(5//2) #integer division :- the actual result is 2.5 but it will return 2 due to the floor division
 
print(5%2)  #modulus operator :- it will return the remainder of the division
 
print(2**3) #exponentiation operator


# ====== Relational Operators ======
# in relational operators we compare two values and return a boolean value (True or False)

print( 5 > 3) #greater than

print( 5 < 3) #less than

print( 5 >= 3) #greater than or equal to

print( 5 <= 3) #less than or equal to

print( 5 == 3) #equal to

print( 5 != 3) #not equal to


# ===== Logical Operators ====== 
#  and , or , not
print( 1 and 0)

print(1 or 0)

print(not 1) #it returns the true and false


# ===== Bitwise Operators ======

print(5 & 3) #bitwise and
print(5 | 3) #bitwise or
print(5 ^ 3) #bitwise xor
print(~5)    #bitwise not
print(5 << 1) #left shift
print(5 >> 1) #right shift


# ===== Assignment Operators ======
x = 5 

# x = x + 3
x += 3 
print(x)


# ===== Membership Operators ======
# in operator :- it checks if a value is present in a sequence (like list, tuple, string) and returns True if it is present, otherwise it returns False
print( 'D' in 'Delhi') # it return True 

print ( 3 in [1,2,3,4,5,6]) # it return True

# not in operator :- it checks if a value is not present in a sequence and returns True if it is not present, otherwise it returns False
print( 'D' not in 'Delhi') # it return False

print( 4 not in [1,2,3,4,5,6]) # it return False


# WAP to find the sum of three numbers entered by the user
a = int(input("Enter first number :")) 
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))
d = a + b + c
print("The sum of three numbers is :" ,d)