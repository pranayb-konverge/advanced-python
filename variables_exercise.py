def moo(list_l):
    list_l.append((1,2))
    list_l[-1] = (("b","c"))
    list_l[0] = {1.1,2.3}
    list_l[0].add(5.5)

list_o = ["a", 3, 4]
moo(list_o)
print(list_o)

