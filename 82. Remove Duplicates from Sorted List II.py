# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Input: head = [1,1,1,2,3]
# Output: [2,3]

# The number of nodes in the list is in the range [0, 300].
#    -100 <= Node.val <= 100
#    The list is guaranteed to be sorted in ascending order.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        prevlist = ListNode(next=head)
        prev, cur = prevlist, head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return prevlist.next
