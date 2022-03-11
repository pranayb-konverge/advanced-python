print('\n----------------------Useful methods in string-----------------------------\n')
# Useful methods in string

my_string = "     Hello World "

# remove white space
my_string = my_string.strip()
print(my_string)

# number of characters
print(len(my_string))

# Upper and lower cases
print(my_string.upper())
print(my_string.lower())

# startswith and endswith
print("hello".startswith("he"))
print("hello".endswith("llo"))

# find first index of a given substring, -1 otherwise
print("Hello".find("o"))

# count number of characters/substrings
print("Hello".count("e"))

# replace a substring with another string (only if the substring is found)
# Note: The original string stays the same
message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

# split the string into a list
my_string = "how are you doing"
string_list = my_string.split() # default argument is " "
print(string_list)

my_string = "one,two,three"
string_list = my_string.split(",")
print(string_list)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
my_string = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(my_string)

print('\n----------------------Useful formating in string-----------------------------\n')
# Useful formating in string

# use braces as placeholders
my_string = "Hello {0} and {1}".format("Peter", "Tom")
print(my_string)

# the positions are optional for the default order
my_string = "Hello {} and {}".format("Peter", "Tom")
print(my_string)

my_string = "The integer value is {}".format(2)
print(my_string)

# some special format rules for numbers
my_string = "The float value is {0:.3f}".format(2.1234)
print(my_string)
my_string = "The float value is {0:e}".format(2.1234)
print(my_string)
my_string = "The binary value is {0:b}".format(2)
print(my_string)

# old style formatting by using % operator
print("Hello %s and %s" % ("Peter", "Tom")) # must be a tuple for multiple arguments
val =  3.14159265359
print("The decimal value is %d" % val)
print("The float value is %f" % val)
print("The float value is %.2f" % val)

#f-string

name = "Peter"
age = 25
my_string = f"Hello, {name}. You are {age}."
print(my_string)
pi = 3.14159
my_string = f"Pi is {pi:.3f}"
print(my_string)
# f-Strings are evaluated at runtime, which allows expressions
my_string = f"The value is {2*60}"
print(my_string)

print('\n----------------------immutability and concatenation in string-----------------------------\n')
# immutability and concatenation in string
from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
my_string = ""
for i in my_list:
    my_string += i
end = timer()
print(f"concatenate string with + : {(end - start):.5f}")

# good
start = timer()
my_string = "".join(my_list)
end = timer()
print(f"concatenate string with join(): {end-start:.5f}")