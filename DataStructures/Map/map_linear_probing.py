class LinearProbingMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def _probe(self, index):
        return (index + 1) % self.capacity
    
    def put(self, key, value):
        if self.size >= self.capacity * 0.7:  # Resize if load factor > 0.7
            self._resize()
        
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value  # Update value if key exists
                return
            index = self._probe(index)  # Linear probing
        
        self.keys[index] = key
        self.values[index] = value
        self.size += 1
    
    def get(self, key):
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._probe(index)  # Linear probing
        
        return None  # Key not found
    
    def remove(self, key):
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.size -= 1
                self._rehash()  # Rehash to maintain integrity
                return True
            index = self._probe(index)  # Linear probing
        
        return False  # Key not found
    
    def _rehash(self):
        old_keys = self.keys[:]
        old_values = self.values[:]
        
        self.capacity = max(10, self.capacity)
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.put(old_keys[i], old_values[i])
    
    def _resize(self):
        old_keys = self.keys[:]
        old_values = self.values[:]
        
        self.capacity *= 2
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.put(old_keys[i], old_values[i])
    
    def __repr__(self):
        return "{" + ", ".join(f"{self.keys[i]}: {self.values[i]}" for i in range(self.capacity) if self.keys[i] is not None) + "}"
