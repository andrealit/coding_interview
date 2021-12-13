from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        # place the cache with capacity size
        self.sz = capacity
        self.dict = OrderedDict()
        # use an ordered dict to maintain the order where we entered values

    def get(self, key: int) -> int:
        if key in self.dict:
            value = self.dict[key] # retrieve the value mapped to the key
            del self.dict[key] # remove the key
            self.dict[key] = value # reassign the key to the value
            return value
        return -1 # doesn't exist

    def put(self, key: int, value: int) -> None:
        if key in self.dict: # key is present, so delete the key and replace with a new value
            del self.dict[key]
            self.dict[key] = value
        elif len(self.dict) < self.sz: # the length of the dictionary is less than the current
            self.dict[key] = value
        else: # remove the last item
            self.dict.popitem(last=False)
            self.dict[key] = value
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)