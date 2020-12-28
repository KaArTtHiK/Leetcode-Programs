#checking whether the linked list is circular or not
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
def circular(head):
    if head == None:
        return True
    i =0
    node = head.next
    while((node is not None) and (node is not head)):
        i = i+1
        node = node.next
    return (node==head)

        
#if __name__ = '__main__':
llist = LinkedList()
llist.head = node(1)
second = node(2)
third = node(3)
fourth = node(4)
llist.head.next = second
second.next = third
third.next =fourth
llist.print_list()
if(circular(llist.head)):
    print("Yes")
else:
    print("No")
fourth.next = llist.head
if(circular(llist.head)):
    print("Yes")
else:
    print("No")
	
	
	
"""
1
2
3
4
No
Yes
"""