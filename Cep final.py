class Node:
    def __init__(self,key, val):
        assert 0<=key<=100, "key should be between 0 and 100"
        assert 0<=val<=100, "value should be between 0 and 100"
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:
    def __init__(self, capacity):
        assert 1<=capacity<=50, "capacity should be between 0 and 50"
        self.cap=capacity
        self.cache={}  # map key to node
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.misses =0
        self.hits =0

    # remove node from list
    def remove(self, node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    
    # insert node at right
    def insert(self, node):
        prev=self.right.prev
        nxt=self.right
        prev.next = nxt.prev = node
        node.next=nxt
        node.prev=prev

    def get(self, key):
        if key in self.cache:
            self.hits +=1
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            self.misses +=1
        return -1
    def put(self, key, val):
        if key in self.cache:
        # Update the value of the existing node (no miss increment)
            node = self.cache[key]
            node.val = val
            self.remove(node)
            self.insert(node)
            self.hits+=1
        else:
        # Create a new node and add it to the cache (this should count as a miss)
            self.misses += 1  # Increment miss for new key insertion
            node = Node(key, val)
            self.cache[key] = node
            self.insert(node)

        if len(self.cache) > self.cap:
            # Remove the LRU node and delete it from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def print_cache(self):
        print(self.cache.keys())
    
    def missrate(self):
        total_access = self.hits + self.misses
        if total_access == 0:
            return None
        return (self.misses / total_access) * 100

#drivers code
# Create cache with capacity 50
cache = LRUCache(50)

# Fill the cache with keys 0 to 49
for i in range(50):
     cache.put(i, i)
print("The Total Hits are: ",cache.hits)
print("The Total Misses are: ",cache.misses)
cache.print_cache()
print()

# Access all odd-numbered keys to update hits/misses
for i in range(100):
     if i%2 !=0:
        cache.get(i)
print("The Total Hits are: ",cache.hits)
print("The Total Misses are: ",cache.misses)
cache.print_cache()
print()

#filling the cache with prime numbers from 0 to 100 
for i in range(100):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count ==2:
        cache.put(i,i)
print("The Total Hits are: ",cache.hits)
print("The Total Misses are: ",cache.misses)
cache.print_cache()
print()

# Print the final miss rate
print("Final Miss Rate:", cache.missrate(), "%")
print()
