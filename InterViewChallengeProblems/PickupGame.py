import random
arr=[]
p1=[0,'karthik']
p2=[0,'karthik2']
p3=[0,'karthik3']
p4=[0,'karthik4']
p5=[0,'karthik5']
tmp=random.randint(1,101)
for i in range(25):
    while tmp in arr:
        tmp=random.randint(1,101)
    arr.append(tmp)
for i in range(0,5):
    p1.insert(i,arr[5*i])
    p2.insert(i,arr[(5*i)+1])
    p3.insert(i,arr[(5*i)+2])
    p4.insert(i,arr[(5*i)+3])
    p5.insert(i,arr[(5*i)+4])
p1[5]=p1[0]+p1[1]+p1[2]+p1[3]+p1[4]
p2[5]=p2[0]+p2[1]+p2[2]+p2[3]+p2[4]
p3[5]=p3[0]+p3[1]+p3[2]+p3[3]+p3[4]
p4[5]=p4[0]+p4[1]+p4[2]+p4[3]+p4[4]
p5[5]=p5[0]+p5[1]+p5[2]+p5[3]+p5[4]
for i in range(0,6):
    if ((p1[i]>p2[i]) and (p1[i]>p3[i]) and (p1[i]>p4[i]) and (p1[i]>p5[i])):
        print(p1[6],end="\n")
    elif ((p2[i]>p3[i]) and (p2[i]>p4[i]) and (p2[i]>p5[i])):
        print(p2[6],end="\n")
    elif ((p3[i]>p4[i]) and (p3[i]>p5[i])):
        print(p3[6],end="\n")
    elif (p4[i]>p5[i]):
        print(p4[6],end="\n")
    else:
        print(p5[6],end="\n")
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)



"""
Input:
No Input

output:
karthik3
karthik4
karthik3
karthik4

Coding Challenge!
In a birthday celebration, the organizers would like to conduct a game to entertain the crowd.
The game rules as follows:
-1 to 100 numbers are available in a jar.
-5 Participants can contest in each slot / session.
-5 slots are available,
-Each participant will get 3 chances to pick the number from the Jar.
-Need to count the numbers picked by individual contestants. Who receives the highest number after counting, he/she is the winner.
-The winner should be displayed for each session


Requirements must be considered
-Numbers should be assigned randomly.
-Contestant names can be generic (Ruby, Rails, Rlya, Richard...)
-Only one number can be picked for each attempt. Same number should not repeat

Optional Requirements
-After picking 3 numbers, the contestant can see his score
-Any other thing mentioned above, you feel must
"""