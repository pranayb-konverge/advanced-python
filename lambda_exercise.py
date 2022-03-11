print('\n----------------------lambda function-----------------------------\n')
# lambda function

add = lambda x: x+10
print(f"Lambda function to add x to 10: {add(3)}")

# get list using lambda
get_list = lambda my_list: [x for x in my_list if x > 2]
print(f"Generate list using lambda function: {get_list([1,2,3,4,5,6])}")

print('\n----------------------sorted function-----------------------------\n')
# sorted function

before_sorted = [(4,5), (2,-1), (1,-1)]
after_sorted = sorted(before_sorted, key=lambda x:x[1])

print(f"Before sorted list: {before_sorted}")
print(f"After dorted list: {after_sorted}")

print('\n----------------------map function-----------------------------\n')
# map function

my_list = [1,2,3,4,5,6]
my_map = map(lambda x : x*2, my_list)
print(f"The mapped list where elemets are squared: {list(my_map)}")

print('\n----------------------filter function-----------------------------\n')
# filter function
my_list = [1,2,3,4,5,6]
my_map = filter(lambda x : x > 4, my_list)
print(f"The filtered list where elemets are greated than 4: {list(my_map)}")
