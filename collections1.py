print('\n----------------------Counter in collections-----------------------------\n')
# Counter in collections

from collections import Counter, namedtuple, defaultdict, deque
a = "aaaaabbbbcccdde"
my_counter = Counter(a)
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
d = defaultdict(int)
d['yellow'] = 1
d['blue'] = 2
print(d.items())
print(d['green'])

# initialize with a default list value, i.e an empty list
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    d[k].append(v)

print(d.items())
print(d['green'])

print('\n----------------------deque in collections-----------------------------\n')
# deque in collections

d = deque()

# append() : add elements to the right end 
d.append('a')
d.append('b')
print(d)

# appendleft() : add elements to the left end 
d.appendleft('c')
print(d)

# pop() : return and remove elements from the right
print(d.pop())
print(d)

# popleft() : return and remove elements from the left
print(d.popleft())
print(d)

# clear() : remove all elements
d.clear()
print(d)

d = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j']) # note that 'j' is now at the left most position
print(d)

# count(x) : returns the number of found elements
print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)