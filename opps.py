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
        self.menu()
    
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
        user_pin = input("Enter your pin :")
        self.pin = user_pin

        user_balance = int(input("Enter your balance :"))
        self.balance = user_balance

        print("Your pin is created successfully")
  
        # call the menu function again to show the menu again
        self.menu()
    
    # change pin function
    def change_pin(self):
        old_pin = input("Enter your old pin :")

        if old_pin == self.pin:
            new_pin = input("Enter your new pin : ")
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
        user_pin=input("Enter your pin :")
        if user_pin == self.pin:
            print("Your balance is :" , self.balance)
        else:
            print("Your pin is incorrect")
    
    def withdraw_cash(self):
        user_pin = input("Enter your pin :")
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