from multiprocessing import Pool

print('\n----------------------Queue in Multi processing-----------------------------\n')
# Queue in Multi processing
# communicate between processes with the multiprocessing Queue
# Queues are thread and process safe
from multiprocessing import Process, Queue

def square(numbers, queue):
    for num in numbers:
        queue.put(num*num)

def make_negative(numbers, queue):
    for num in numbers:
        queue.put(num*-1)

if __name__ == "__main__":
    
    numbers = range(1, 6)
    q = Queue()

    process_1 = Process(target=square, args=(numbers,q))
    process_2 = Process(target=make_negative, args=(numbers,q))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    # order might not be sequential
    while not q.empty():
        print(q.get())

print('\n----------------------Multi processing pool-----------------------------\n')
# Multi processing pool

def square(num):
    return num * num

if __name__ == "__main__":
    numbers = range(6)

    pool = Pool()
    result = pool.map(square, numbers)
    pool.close()
    pool.join()

    print(result)