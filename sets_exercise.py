print('\n----------------------Create sets-----------------------------\n')
# Create Sets

my_set_fruits = {"apple", "banana", "cherry"}
print(my_set_fruits)

# or use the set function and create from an iterable, e.g. list, tuple, string
my_set_numbers = set(["one", "two", "three"])
my_set_numbers = set(("one", "two", "three"))
# my_set_numbers = set(("one", "two", "three"), (1,2,3)) # This is an error case
print(my_set_numbers)

my_set_string = set("aaabbbcccdddeeeeeffff")
print(my_set_string)

# careful: an empty set cannot be created with {}, as this is interpreted as dict
# use set() instead
my_dict = {}
print("Type of a={}: ",type(my_dict))
my_set = set()
print("Type of a=set(): ",type(my_set))

print('\n----------------------Add element in sets-----------------------------\n')
# Add element in Sets

my_set = set()

# use the add() method to add elements
my_set.add(55)
my_set.add(54.56)
my_set.add("55")
my_set.add(True)

print(my_set) # note: the order does not matter, and might differ when printed

# nothing happens when the element is already present:
my_set.add(55)
print(my_set)

print('\n----------------------Remove element from sets-----------------------------\n')
# Remove element from Sets

# remove(x): removes x, raises a KeyError if element is not present
my_set_fruits = {"apple", "banana", "cherry"}
my_set_fruits.remove("apple")
print(my_set_fruits)

# KeyError:
# my_set_fruits.remove("orange")

# discard(x): removes x, does nothing if element is not present
my_set_fruits.discard("cherry")
my_set_fruits.discard("blueberry") # better to use discard
print(my_set_fruits)

# clear() : remove all elements
my_set_fruits.clear()
print(my_set_fruits)

# pop() : return and remove a random element
my_set_random_elements = {True, 2, False, "hi", "hello"}
print(my_set_random_elements.pop()) # pop() takes no arguments
print(my_set_random_elements)

print('\n----------------------Union and Intersection in sets-----------------------------\n')
# Union and Intersection in sets

odds_set = {1, 3, 5, 7, 9}
evens_set = {0, 2, 4, 6, 8}
primes_set = {2, 3, 5, 7}

# union() : combine elements from both sets, no duplication
# note that this does not change the two sets
union_set = odds_set.union(evens_set)
print(union_set)

# intersection(): take elements that are in both sets
intersection_set = odds_set.intersection(evens_set)
print(intersection_set)

intersection_set = odds_set.intersection(primes_set)
print(intersection_set)

intersection_set = evens_set.intersection(primes_set)
print(intersection_set)

print('\n----------------------Difference of sets-----------------------------\n')
# Difference of sets

num_set_long = {1, 2, 3, 4, 5, 6, 7, 8, 9}
num_set_short = {1, 2, 3, 10, 11, 12}

# difference() : returns a set with all the elements from the num_set_long that are not in num_set_short.
diff_set = num_set_long.difference(num_set_short)
print(diff_set)

# A.difference(B) is not the same as B.difference(A)
diff_set = num_set_short.difference(num_set_long)
print(diff_set)

# symmetric_difference() : returns a set with all the elements that are in num_set_long and num_set_short but not in both
diff_set = num_set_long.symmetric_difference(num_set_short)
print(diff_set)

# A.symmetric_difference(B) = B.symmetric_difference(A)
diff_set = num_set_short.symmetric_difference(num_set_long)
print(diff_set)

print('\n----------------------Updating sets-----------------------------\n')
# Updating sets

num_set_long = {1, 2, 3, 4, 5, 6, 7, 8, 9}
num_set_short = {1, 2, 3, 10, 11, 12}

# update() : Update the set by adding elements from another set.
num_set_long.update(num_set_short)
print(num_set_long)

# intersection_update() : Update the set by keeping only the elements found in both
num_set_long = {1, 2, 3, 4, 5, 6, 7, 8, 9}
num_set_long.intersection_update(num_set_short)
print(num_set_long)

# difference_update() : Update the set by removing elements found in another set.
num_set_long = {1, 2, 3, 4, 5, 6, 7, 8, 9}
num_set_long.difference_update(num_set_short)
print(num_set_long)

# symmetric_difference_update() : Update the set by only keeping the elements found in either set, but not in both
num_set_long = {1, 2, 3, 4, 5, 6, 7, 8, 9}
num_set_long.symmetric_difference_update(num_set_short)
print(num_set_long)

# Note: all update methods also work with other iterables as argument, e.g lists, tuples
num_set_long = {1, 2, 3, 10, 11, 12}
num_set_long.update([1, 2, 3, 4, 5, 6])
print(num_set_long)

print('\n----------------------Copying sets-----------------------------\n')
# Copying sets

set_org = {1, 2, 3, 4, 5}

# this is same as tuple
# this just copies the reference to the set, so be careful
set_copy = set_org

# now modifying the copy also affects the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

# use copy() to actually copy the set
set_org = {1, 2, 3, 4, 5}
set_copy = set_org.copy()

# now modifying the copy does not affect the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

print('\n----------------------Subset, Superset, and Disjoint sets-----------------------------\n')
# Subset, Superset, and Disjoint sets
num_set_long = {1, 2, 3, 4, 5, 6}
num_set_short = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
print(num_set_long.issubset(num_set_short))
print(num_set_short.issubset(num_set_long)) # True

# issuperset(setX): Returns True if the set contains setX
print(num_set_long.issuperset(num_set_short)) # True
print(num_set_short.issuperset(num_set_long))

# isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
setC = {7, 8, 9}
print(num_set_long.isdisjoint(num_set_short))
print(num_set_long.isdisjoint(setC))
print(num_set_short.isdisjoint(setC))

print('\n----------------------Frozen sets-----------------------------\n')
# Frozen sets, MOSTLY USED FOR COMPARISION!

a = frozenset([0, 1, 2, 3, 4])

# The following is not allowed:
# a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear()

# Also no update methods are allowed:
# a.update([1,2,3])

# Other set operations work
odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))