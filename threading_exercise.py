print('\n----------------------Multi threading-----------------------------\n')
# Multi threading

from threading import Thread, Lock, current_thread
from queue import Queue
import time

def print_num(q,lock):
    while True:
        value = q.get()
        with lock:
            print(f"I got {value} in {current_thread().name}")
            time.sleep(0.5)
        
        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()

if __name__ == "__main__": 
    # generate numbers and assign to queue 
    q = Queue()
    for r in range(20):
        q.put(r)
    print("Items in global queues: ",q.queue)

    num_threads = 3
    lock = Lock()
    # create threads and asign a function for each thread
    for t in range(num_threads):
        thread = Thread(target=print_num, args=(q,lock))
        thread.daemon = True
        thread.start()
     
    q.join()  # Blocks until all items in the queue have been gotten and processed.
