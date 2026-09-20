class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        # if key in self.cache:
        #     self.cache.move_to_end(key)
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            delete = None
            for key in self.cache.keys():
                delete = key
                break
            del self.cache[delete]
