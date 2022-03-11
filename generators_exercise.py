print('\n----------------------generator function-----------------------------\n')
# generator function

import sys

list_even_num = [x for x in range(1000000) if x%2==0]
gen_even_num = (x for x in range(1000000) if x%2==0)

print(sum(list_even_num), "Sum")
print(sys.getsizeof(list_even_num), "bytes")
print()
print(sum(gen_even_num), "Sum")
print(sys.getsizeof(gen_even_num), "bytes") # less memory space