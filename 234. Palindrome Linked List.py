# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # this is mid of the linked list
        # return slow   

        # reverse the second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        # return prev # this is reversed list
        
        # compare
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
    