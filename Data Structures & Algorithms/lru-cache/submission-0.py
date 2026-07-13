class Node:
    def __init__(self, key=0, value=0):
        # initialize a new node with a key, value, and prev/next pointers
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head,self.tail = Node(0,0),Node(0,0)
        self.tail.next, self.head.prev = self.head,self.tail     
        
    def insert(self,node):
        left,right = self.head.prev,self.head
        left.next=right.prev = node
        node.prev,node.next= left,right
    
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next ,nxt.prev = nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.tail.next
            self.remove(lru)
            del self.cache[lru.key]
        
