print('----------------------Tiple Methods-----------------------------')
# Tiple Methods
my_tuple = ('a','p','p','l','e',)

# print the tuple
print("The original tuple: " + str(my_tuple))

# len() : get the number of elements in a tuple
print("Length of Tuple: " + str(len(my_tuple)))

# count(x) : Return the number of items that is equal to x
letter = 'p'
print("Count of words or letter - "+letter+", in Tuple: " + 
str(my_tuple.count(letter)))

# index(x) : Return index of first item that is equal to x
letter = 'e'
print("The index of letter - "+letter+", in Tuple: " + 
str(my_tuple.index(letter)))

# repetition
my_tuple = ('a', 'b') * 5
print("Result of ('a', 'b') * 5: "+ str(my_tuple))

# concatenation
my_tuple = (1,2,3) + (4,5,6)
print("Result of (1,2,3) + (4,5,6): "+ str(my_tuple))

# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)

print('----------------------Slicing-----------------------------')
#Slicing

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a[:]) # a[start:stop:step], default step is 1

b = a[1:3] # Note that the last index is not included
print(b)

b = a[2:] # until the end
print(b)

b = a[:3] # from beginning
print(b)

b = a[::2] # start to end with every second item
print(b)

b = a[::-1] # reverse tuple
print(b)

print('----------------------Unpack tuple-----------------------------')
# Unpack tuple
# number of variables have to match number of tuple elements
tuple_1 = ("Max", 28, "New York")
name, age, city = tuple_1
print(name)
print(age)
print(city)
print()
# tip: unpack multiple elements to a list with *
my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(item_first)
print(items_between) # list is created
print(item_last)

print('----------------------Compare tuple and list-----------------------------')
# Compare tuple and list
# compare the size
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
# print the tuple
print("The original tuple: " + str(my_tuple))
# print the list
print("The original list: " + str(my_list))
print()

print("Size of list: ", sys.getsizeof(my_list), "bytes")
print("Size of tuple: ", sys.getsizeof(my_tuple), "bytes")
print()

# compare the execution time of a list vs. tuple creation statement
import timeit
print("Execution time of list: ", 
timeit.timeit(stmt='[0, 1, 2, "hello", True]', number=1000000))

print("Execution time of tuple: ", 
timeit.timeit(stmt='(0, 1, 2, "hello", True)', number=1000000))