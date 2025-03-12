class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SeparateChainingMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        index = self._hash(key)
        
        if self.buckets[index] is None:
            self.buckets[index] = Node(key, value)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value  # Update existing key
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)
        
        self.size += 1
        if self.size > self.capacity * 0.7:
            self._resize()
    
    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None  # Key not found
    
    def remove(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        
        return False  # Key not found
    
    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [None] * self.capacity
        
        for bucket in old_buckets:
            current = bucket
            while current:
                self.put(current.key, current.value)
                current = current.next
    
    def __repr__(self):
        result = "{"
        for bucket in self.buckets:
            current = bucket
            while current:
                result += f"{current.key}: {current.value}, "
                current = current.next
        return result.rstrip(", ") + "}"
