l = [1,4,5,6,7,2,3,4]
def b(l):
    for i in range(1,len(l)):
        j= i-1
        nex = l[j+1]
        while(j>= 0 and l[j] > nex):
            l[j+1] = l[j]
            l[j] = nex
            j = j-1
b(l)
print(l)