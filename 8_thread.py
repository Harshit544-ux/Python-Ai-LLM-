# # how to check the main thread in python

# import threading
# # to check the main thread in python
# print(threading.current_thread()) 
# # to check the name of the current thread
# print(threading.current_thread().name) 
# # to check the id of the current thread
# print(threading.current_thread().ident)
# # to check if the current thread is alive or not
# print(threading.current_thread().is_alive())


# there are two way to create a thread in python
# 1)by using thread class present in threading module
# 2)by extending Thread class (inheritance)


# 1) by using thread class present in threading module

# steps :-
# (a) Import Thread class from threading module
# (b) Create a function containing code to be executed parallelly
# (c) Create a Thread object and pass the function as target to the Thread class
# (d) Start the thread using start() method

# Implementation :- 

# import Thread class
from threading import Thread ,current_thread

# Create a function containing code to be executed parallelly
def display(n,msg):
    print("t1 thread : " , current_thread().name)
    for i in range(n):
        print(msg)
    
# create a new Thread Here
t1=Thread(target=display,args=(5,'Hello World'))
# start the new Thread
t1.start()

# this run by main thread
for i in range(5):
    print("Main Thread")