class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.age_bits = dict()

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        
        # 1 + max(all bits)
        self.age_bits[key] = max(self.age_bits.values())+1

        return self.cache[key]

    def _lowest_bit(self):
        keys = list(self.age_bits.keys())
        values = [self.age_bits[k] for k in keys]
        currmin = max(values)
        ix = 0
        for i in range(len(values)):
            if values[i] < currmin:
                currmin = values[i]
                ix = i
        
        return keys[ix]

    def put(self, key: int, value: int) -> None:

        if key in self.cache.keys():
            self.cache[key] = value
            # Update bit
            self.age_bits[key] = max(self.age_bits.values())+1
        else:
            
            # If empty
            if len(self.cache.keys()) == 0:
                self.age_bits[key] = 0
                self.cache[key] = value
            elif 0 < len(self.cache.keys()) < self.capacity:
                self.cache[key] = value
                # Update time.
                self.age_bits[key] = max(self.age_bits.values())+1
            else:
                
                # print(self.cache)
                
                # Find key to evict.
                key_to_evict = self._lowest_bit()

                # Delete key
                del self.cache[key_to_evict]
                del self.age_bits[key_to_evict]

                # Replace.
                self.cache[key] = value
                
                if len(self.age_bits.keys()) == 0:
                    self.age_bits[key] = 0
                else:
                    self.age_bits[key] = max(self.age_bits.values())+1


# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    # obj = LRUCache(2)
    
    # print(obj.put(1, 1))
    # print(obj.put(2, 2))
    # print(obj.get(1))
    # print(obj.put(3, 3))
    # print(obj.get(2))
    # print(obj.put(4, 4))
    # print(obj.get(1))
    # print(obj.get(3))
    # print(obj.get(4))
    
    # # null, null, 1, null, -1, null, -1, 3, 4
    
    # [[1],[2,1],[2],[3,2],[2],[3]]
    obj = LRUCache(1)
    print(obj.put(2, 1))
    print(obj.get(2))
    print(obj.put(3, 2))
    print(obj.get(2))
    print(obj.get(3))
