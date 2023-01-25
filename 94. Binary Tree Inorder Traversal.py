# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root, out):
    if root is None:
        return
    dfs(root.left, out)
    out.append(root.val)
    dfs(root.right, out)
    return out

class Solution:    
    def inorderTraversal(self, root: TreeNode):
        return dfs(root,[])