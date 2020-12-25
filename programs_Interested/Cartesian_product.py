from itertools import product
l1 = ['a','b','c']
l2 = ['d','e','f']
l3 = product(l1,l2)
for x,y in list(l3):
    print(x+y)


"""
ad
ae
af
bd
be
bf
cd
ce
cf
"""