# 1) if else :- 
# login program and identation

email = input ("Enter your email :")
password = input("Enter your password :")

if email == "harshitsri08@gmail.com" and password == "harshit123":
    print("Login Successfully")
else:
    print("Invalid email or password")


# 2) elif :-

# take the input 
email = input("Enter your email: ")
password = input("Enter your password: ")

# check the email and password
if email == "abc@gmail.com" and password == "abc123":
    print("Login Successfully")

elif email == "abc@gmail.com" and password != "abc123":
    # tell the user
    print("Invalid password")
    # taking again input for password
    password = input("Enter your password again: ")
    
    # password is correct or not
    if password == "abc123":
        print("Login Successfully after retry")
    else:
        print("Login Failed after retry")

# if email is wrong
else:
    print("Invalid email")