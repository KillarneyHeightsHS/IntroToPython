# Custom Hash Table implementation
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists for chaining
    
    def _hash(self, key):
        """Simple hash function"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        
        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)
    
    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example usage
ht = HashTable()
ht.insert("name", "John")
ht.insert("age", 30)
ht.insert("city", "New York")

print(ht.get("name"))  # John
ht.display()

# Word frequency counter using hash table
def count_words(text):
    word_count = {}
    words = text.lower().split()
    
    for word in words:
        # Remove punctuation
        word = word.strip(".,!?;:")
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

text = "The quick brown fox jumps over the lazy dog. The dog was lazy."
frequencies = count_words(text)
print(frequencies)