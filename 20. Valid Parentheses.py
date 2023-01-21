# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.


# Input: s = "()[]{}"
# Output: true

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        stack = deque()
        
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if len(stack) >= 1:
                    if s[i] == ')' and stack[-1] == '(':
                        stack.pop()
                    elif s[i] == '}' and stack[-1] == '{':
                        stack.pop()
                    elif s[i] == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else: 
                    return False
        if len(stack) >= 1:
            return False
        else:
            return True