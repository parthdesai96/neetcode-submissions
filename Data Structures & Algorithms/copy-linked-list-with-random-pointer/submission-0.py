"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}
        curr = head
        while curr:
            clone = Node(curr.val)
            oldToCopy[curr] = clone
            curr = curr.next
        curr = head
        while curr:
            clone = oldToCopy[curr]
            clone.next = oldToCopy[curr.next]
            clone.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]
        