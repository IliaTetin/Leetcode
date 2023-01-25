# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [3,2,1]

# The number of the nodes in the tree is in the range [0, 100].
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
    dfs(root.right, out)
    out.append(root.val)
    return out

class Solution:
    def postorderTraversal(self, root: TreeNode):
        return dfs(root, [])