print('\n----------------------Counter in collections-----------------------------\n')
# Counter in collections

from collections import Counter, namedtuple, defaultdict, deque
my_string = "aaaaabbbbcccdde"
my_counter = Counter(my_string)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

# most common items
print(my_counter.most_common(1))

# Return an iterator over elements repeating each as many times as its count. 
# Elements are returned in arbitrary order.
print(list(my_counter.elements()))

print('\n----------------------namedtuple in collections-----------------------------\n')
# namedtuple in collections
# ref - https://towardsdatascience.com/understand-how-to-use-namedtuple-and-dataclass-in-python-e82e535c3691

# create a namedtuple with its class name as string and its fields as string
# fields have to be separated by comma or space in the given string
# Named Tuple allows us to give names to the elements, so we can access the 
# attributes by both attribute name and its index.

# Quikest way to create a class with fields which are quick to searcha and modify.
Transaction = namedtuple('Transaction',['sender','amount','receiver','date'])

record = Transaction(sender="Pranay",amount=108118,receiver="CS",date="07/03/2022")
print(record)
print(record._fields)
print(type(record))
print(record.sender, record.receiver)
print()

# Assigning attributes with a default value is also possible.
TransactionDefault = namedtuple('TransactionDefault',['sender','amount','receiver','date'],
            defaults=["Konverge.ai",135000,"Pranay","02/04/2022"])

record = TransactionDefault()
print(record)
print(record._fields)
print(record._field_defaults)
print(type(record))
print(record.sender, record.receiver)
print(record._asdict())

print('\n----------------------defaultdict in collections-----------------------------\n')
# defaultdict in collections

# initialize with a default integer value, i.e 0
my_defualt_int_dictionary = defaultdict(int)
my_defualt_int_dictionary['yellow'] = 1
my_defualt_int_dictionary['blue'] = 2
print(my_defualt_int_dictionary.items())
print(my_defualt_int_dictionary['green'])

# initialize with a default list value, i.e an empty list
my_defualt_list_dictionary = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    my_defualt_list_dictionary[k].append(v)

print(my_defualt_list_dictionary.items())
print(my_defualt_list_dictionary['green'])

print('\n----------------------deque in collections-----------------------------\n')
# deque in collections

"""

A deque is a double-ended queue. It can be used to add or remove elements from both ends. 
Deques support thread safe, memory efficient appends and pops from either side of the deque 
with approximately the same O(1) performance in either direction. The more commonly used s
tacks and queues are degenerate forms of deques, where the inputs and outputs are 
restricted to a single end.

"""

my_deque = deque()

# append() : add elements to the right end 
my_deque.append('a')
my_deque.append('b')
print(my_deque)

# appendleft() : add elements to the left end 
my_deque.appendleft('c')
print(my_deque)

# pop() : return and remove elements from the right
print(my_deque.pop())
print(my_deque)

# popleft() : return and remove elements from the left
print(my_deque.popleft())
print(my_deque)

# clear() : remove all elements
my_deque.clear()
print(my_deque)

my_deque = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
my_deque.extend(['e', 'f', 'g'])
my_deque.extend(['e', 'f', 'g'])
my_deque.extendleft(['h', 'i', 'j']) # note that 'j' is now at the left most position
print(my_deque)

# count(x) : returns the number of found elements
print(my_deque.count('h'))

# rotate 1 positions to the right
my_deque.rotate(1)
print(my_deque)

# rotate 2 positions to the left
my_deque.rotate(-2)
print(my_deque)