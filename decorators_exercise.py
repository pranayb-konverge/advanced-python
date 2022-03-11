print('\n----------------------decorator function-----------------------------\n')
# decorator function
import functools
import random
import time

def cal_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result  = func(*args, **kwargs)
        print(f"Total {(time.time() - start)} seconds needed to run the function.")
        return result
    return wrapper

@cal_time
def generate_random(print_var):
    print(print_var)
    print("Random number: ",random.randint(1,100))

generate_random("This is a random generator function with decorator to check the start and end time.") 