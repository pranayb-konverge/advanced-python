print('----------------------Create Dictionary-----------------------------')
# Create Dictionary
my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)

# or use the dict constructor, note: no quotes necessary for keys
my_dict_new = dict(name="Lisa", age=27, city="Boston")
print(my_dict_new)

print('----------------------CRUD Dictionary-----------------------------')
# CRUD Dictionary
# get the 'name' value
name_in_dict = my_dict_new["name"]
print(name_in_dict)

# add/update the key values 
print(my_dict_new)
my_dict_new["age"] = 25
my_dict_new["email"] = "something123@somthind.com"
print(my_dict_new)

# delete a key-value pair
del my_dict_new["email"]

# this returns the value and removes the key-value pair
print("popped value:", my_dict_new.pop("age"))

# return and removes the last inserted key-value pair 
# (in versions before Python 3.7 it removes an arbitrary pair)
print("popped item:", my_dict_new.popitem())
print(my_dict_new)
print()

# remove all pairs
print(my_dict)
my_dict.clear()
print(my_dict)
print()

# create dict using tuple of tuples
my_tuple = (("string_key1", 23), ("string_key2", 33))
tuple_dict = dict(my_tuple)
print("create dict using tuple of tuples: ",tuple_dict)

print('----------------------Check for keys in Dictionary-----------------------------')
# Check for keys in Dictionary
my_dict = {"name":"Max", "age":28, "city":"New York"}
# use if .. in ..
if "name" in my_dict:
    print(my_dict["name"])

# use try except
try:
    print(my_dict["firstname"])
except KeyError:
    print("No key found")

print('----------------------Copy a Dictionary-----------------------------')
# Copy a Dictionary
dict_org = {"name":"Max", "age":28, "city":"New York"}

# this just copies the reference to the dict, so be careful
dict_copy = dict_org

# now modifying the copy also affects the original
dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

# use copy(), or dict(x) to actually copy the dict
dict_org = {"name":"Max", "age":28, "city":"New York"}

dict_copy = dict_org.copy()
# dict_copy = dict(dict_org)

# now modifying the copy does not affect the original
dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_new = dict(name="Lisa", age=27, city="Boston")

# extend/merge dictionaries
my_d = my_dict.update(my_dict_new)
print(my_d) # no assignment so empty
print(my_dict) # updated

print("--------------------------Possible key types in Dict----------------")
# Possible key types in Dict
# use numbers as key, but be careful
my_dict = {3: 9, 6: 36, 9:81}
# do not mistake the keys as indices of a list, e.g my_dict[0] is not possible here
print(my_dict[3], my_dict[6], my_dict[9])

# use a tuple as key with immutable elements (e.g. number, string)
my_tuple = (8, 7)
my_dict = {my_tuple: 15}

print(my_dict[my_tuple])
print(my_dict[8, 7])
print(my_dict)