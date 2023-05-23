# SuperFastPython.com
# example of a thread-safe list
from threading import Thread
from threading import Lock
 
# custom class wrapping a list in order to make it thread safe
class ThreadSafeList():
    # constructor
    def __init__(self):
        # initialize the list
        self._list = list()
        # initialize the lock
        self._lock = Lock()
 
    # add a value to the list
    def append(self, value):
        # acquire the lock
        with self._lock:
            # append the value
            self._list.append(value)
 
    # remove and return the last value from the list
    def pop(self):
        # acquire the lock
        with self._lock:
            # pop a value from the list
            return self._list.pop()
 
    # read a value from the list at an index
    def get(self, index):
        # acquire the lock
        with self._lock:
            # read a value at the index
            return self._list[index]
 
    # return the number of items in the list
    def length(self):
        # acquire the lock
        with self._lock:
            return len(self._list)
 
# add items to the list
def add_items(safe_list):
    for i in range(100000):
        safe_list.append(i)
 
# create the thread safe list
safe_list = ThreadSafeList()
# configure threads to add to the list
threads = [Thread(target=add_items, args=(safe_list,)) for i in range(10)]

print(len(threads))

# start threads
for thread in threads:
    thread.start()
# wait for all threads to terminate
print('Main waiting for threads...')
for thread in threads:
    thread.join()
# report the number of items in the list
print(f'List size: {safe_list.length()}')