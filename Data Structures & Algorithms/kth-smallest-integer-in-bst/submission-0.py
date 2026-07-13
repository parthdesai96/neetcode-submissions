# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        value = 0
        smallest = []

        def inOrder(node):
            if not node:
                return 
            inOrder(node.left)
            smallest.append(node.val)
            inOrder(node.right)

        inOrder(root)
        print(smallest)
       
        value = smallest[k-1]
        return value

        