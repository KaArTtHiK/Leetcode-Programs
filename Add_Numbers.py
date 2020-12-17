# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a,b = [],[]
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        
        a.reverse()
        n1 = int("".join(str(i) for i in a))
        
        b.reverse()
        n2 = int("".join(str(i) for i in b))
        
        sum1 = n1 +n2
        sum1 = list(map(int,str(sum1)))
        
        l3 = None
        for i in sum1:
            l3 = ListNode(i,l3)
        
        return l3
        
		
"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""