r, c = map(int,input().strip().split())
res = list()
for i in range(r):
    l = list(map(int,input().strip().split()))
    res.append(l)
for i in zip(*res):
    print(*i)
	
	
"""
Input:
3 5 
13 4 8 14 1
9 6 3 7 21
5 12 17 9 3

output:
13 9 5
4 6 12
8 3 17
14 7 9
1 21 3
"""