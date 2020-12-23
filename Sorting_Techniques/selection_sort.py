l= [1,9,6,8,5,3,2,8765]
def s(l):
    for i in range(len(l)):
        mi = i
        for j in range(i+1,len(l)):
            if l[mi] > l[j]:
                mi = j
        l[i] , l[mi] = l[mi],l[i]
s(l)
print(*l)