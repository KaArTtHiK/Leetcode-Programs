l = [1,2,3,4,5,6]
l1 = [11,12,13,14,15,16]
l2 = [21,22,23,24,25,26]
for i in zip(l,l1,l2):
    print(*i)
	
	
"""
output:
1 11 21
2 12 22
3 13 23
4 14 24
5 15 25
6 16 26

transpose of list elements using zip function
"""