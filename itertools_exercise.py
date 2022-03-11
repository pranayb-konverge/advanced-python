print('\n----------------------product in itertools-----------------------------\n')
# product in itertools

from itertools import product, permutations, combinations, combinations_with_replacement
from itertools import accumulate, groupby, count, cycle, repeat 

prod = product([1, 2], [3, 4])
print(list(prod)) # note that we convert the iterator to a list for printing

# to allow the product of an iterable with itself, specify the number of repetitions 
prod = product([1, 2], [3], repeat=2)
print(list(prod)) # note that we convert the iterator to a list for printing

print('\n----------------------permutations in itertools-----------------------------\n')
# permutations in itertools

perm = permutations([1, 2, 3])
print(list(perm))

# optional: the length of the permutation tuples
perm = permutations([1, 2, 3], 2)
print(list(perm))

print('\n----------------------combinations in itertools-----------------------------\n')
# combinations in itertools

# the second argument is mandatory and specifies the length of the output tuples.
comb = combinations([1, 2, 3, 4], 2)
print(list(comb))

comb = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(comb))

print('\n----------------------accumulate in itertools-----------------------------\n')
# accumulate in itertools

# return accumulated sums
acc = accumulate([1,2,3,4])
print(list(acc))

# other possible functions are possible
import operator
acc = accumulate([1,2,3,4], func=operator.mul)
print(list(acc))

acc = accumulate([1,5,2,6,3,4], func=max)
print(list(acc))

print('\n----------------------groupby in itertools-----------------------------\n')
# groupby in itertools

# or use a lamda expression, e.g. words with an 'i':
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))

print('\n----------------------Infinite iterators in itertools-----------------------------\n')
# Infinite iterators in itertools

# count(x): count from x: x, x+1, x+2, x+3...
for i in count(3):
    print(i)
    if  i >= 10:
        break

# cycle(iterable) : cycle infinitely through an iterable
print("")
sum = 0
for i in cycle([1, 2, 3]):
    print(i)
    sum += i
    if sum >= 12:
        break

# repeat(x): repeat x infinitely or n times
print("")
for i in repeat("A", 3):
    print(i)