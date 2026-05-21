# how to check the main thread in python

import threading
# to check the main thread in python
print(threading.current_thread()) 
# to check the name of the current thread
print(threading.current_thread().name) 
# to check the id of the current thread
print(threading.current_thread().ident)
# to check if the current thread is alive or not
print(threading.current_thread().is_alive())