l = [14,3,2,5,1,7]
for i in range(len(l)-1):
    for j in range(i,len(l)):
        if l[j]<l[i]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(*l)



#1 2 3 5 7 14