print('\n----------------------lambda function-----------------------------\n')
# lambda function

add = lambda x: x+10
print(add(3))

# get list using lamnda
get_list = lambda list_1: [x for x in list_1 if x > 2]
print(get_list([1,2,3,4,5,6]))

print('\n----------------------sorted function-----------------------------\n')
# sorted function

before_sorted = [(4,5), (2,-1), (1,-1)]
after_sorted = sorted(before_sorted, key=lambda x:x[1])

print(before_sorted)
print(after_sorted)

print('\n----------------------map function-----------------------------\n')
# map function

list_1 = [1,2,3,4,5,6]
map_1 = map(lambda x : x*2, list_1)
print(list(map_1))

print('\n----------------------filter function-----------------------------\n')
# filter function
list_1 = [1,2,3,4,5,6]
map_1 = filter(lambda x : x > 4, list_1)
print(list(map_1))
