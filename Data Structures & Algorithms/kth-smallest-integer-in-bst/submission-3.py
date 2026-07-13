# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        value = root.val

        def dst(node):
            nonlocal count,value
            if not node:
                return
            
            dst(node.left)
            count =count- 1
            if count == 0:
                value = node.val
                return
            dst(node.right)
        
        dst(root)
        return value