# class and object in python

# class is a blueprint 
# How to make a class in python

# class naming convention : class name should be in PascalCase
# eg : MyIndia , MyCountry ,Student , Employee etc

# how to create a object
# object = class_name()
# eg: obj = Atm()

class Atm :
    # constructor : (special function) - > superpower -> which does not need to be call explicitly
    def __init__(self):
        self.pin=''
        self.balance=0
        # self.menu()
    
    # menu function
    def menu(self):
        user_input=input("""
         Hi How can I help you ?
         1.Create a Pin
         2.Change a Pin
         3.Check Balance
         4.Withdraw Cash
         5.Anything else to exit
         """)
        
        if user_input=='1':
            # create a pin
            self.create_pin()
        elif user_input == '2':
            # change a pin
             self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw cash
            self.withdraw_cash()
        else:
            exit()
    
    # create pin function
    def create_pin(self):
        user_pin = int(input("Enter your pin :"))
        self.pin = user_pin

        user_balance = int(input("Enter your balance :"))
        self.balance = user_balance

        print("Your pin is created successfully")
  
        # call the menu function again to show the menu again
        self.menu()
    
    # change pin function
    def change_pin(self):
        old_pin = int(input("Enter your old pin :"))

        if old_pin == self.pin:
            new_pin = int(input("Enter your new pin : "))
            self.pin = new_pin
            print("Your pin is changed successfully")
            # call the menu function again to show the menu again
            self.menu()
        else:
            print("Your old pin is incorrect")
            # call the menu function again to show the menu again
            self.menu()
    
    # check balance function
    def check_balance(self):
        user_pin=int(input("Enter your pin :"))
        if user_pin == self.pin:
            print("Your balance is :" , self.balance)
        else:
            print("Your pin is incorrect")
    
    # withdraw cash function
    def withdraw_cash(self):
        user_pin = int(input("Enter your pin :"))
        if user_pin == self.pin:
            amount = int(input("Enter the amount you want to withdraw :"))
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print("Please collect your cash")
                print("Your remaining balance is :" , self.balance)

        else:
            print("Your pin is incorrect")
            self.menu()


 

# creating an object of the class
obj =Atm()
# print(type(obj))


# class Student:
#     def __init__(self):
#         print("database connected successfully")


# obj1 = Student()



class Python:
    def __init__(self,name):
        self.name=name
    
    def printName(self):
        print("Hi I m " , self.name)

p = Python("Harshit")
p.printName()

# parameterized constructor : constructor which takes parameters is called parameterized constructor
class Car:
    def __init__(self,name, price):
        self.name=name
        self.price=price
    
    def details(self):
        print("the car name is ",self.name ,"car price is ",self.price)
        
c= Car("BMW",5000)
c.details()


# Multiple Objects (same class, different data)
class Students:
    def __init__(self,name):
        self.name = name


s1=Students("Harshit")
s2=Students("Garvit")
s3=Students("Arpit")

print(s1.name)
print(s2.name)
print(s3.name)


# Enacpsulation : binding data and functions together in a single unit is called encapsulation
class Bank_account:
    # constructor
    def __init__(self,balance):
        # private variable
        self.__balance=balance 
    
    def deposit(self,amount):
         self.__balance += amount
    
    def get_amount(self):
        return self.__balance


user=Bank_account(1000)
user.deposit(500)
print("the total balance is :", user.get_amount())
# print(user.__balance)  // this will give an error because __balance is a private variable

# How to object access to the attributes and methods
